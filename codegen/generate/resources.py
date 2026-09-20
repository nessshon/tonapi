import textwrap
from pathlib import Path

from codegen.formatter import run_ruff
from codegen.spec import (
    group_endpoints_by_tag,
    operation_to_method_name,
    param_default,
    param_python_type,
    ref_name,
    resolve_parameter,
    resolve_request_body,
    resolve_response_type,
)
from codegen.utils import (
    NON_MODEL_TYPES,
    ROOT,
    env,
    load_config,
    load_spec,
    tag_to_class_name,
    tag_to_module_name,
    to_python_name,
)

RESOURCES_DIR: Path = ROOT / "pytonapi" / "rest" / "resources"
MAX_LINE_LENGTH: int = 120


def _format_docstring(
    description: str,
    params: list[tuple[str, str]],
    return_type: str | None,
    indent: int = 8,
) -> list[str]:
    """Format a reStructuredText docstring.

    :param description: method description text.
    :param params: list of ``(python_name, description)`` tuples.
    :param return_type: return type name, or ``None``.
    :param indent: indentation level in spaces.
    :return: list of docstring lines.
    """
    if not description and not params and not return_type:
        return []

    prefix = " " * indent
    max_width = MAX_LINE_LENGTH - indent

    if description:
        description = description.rstrip()
        description = description.replace("\u2018", "'").replace("\u2019", "'")
        description = description.replace("\u201c", '"').replace("\u201d", '"')
        first_space = description.find(" ")
        if first_space > 0:
            first_word = description[:first_space]
            if first_word.endswith("s") and not first_word.endswith(("ss", "us", "is")):
                description = first_word[:-1] + description[first_space:]
        if not description.endswith("."):
            description += "."

    if not params and not return_type and description:
        single = f'{prefix}"""{description}"""'
        if len(single) <= MAX_LINE_LENGTH and "\n" not in description:
            return [single]

    lines: list[str] = []

    if description:
        first_line = f'{prefix}"""{description}'
        if len(first_line) <= MAX_LINE_LENGTH:
            lines.append(first_line)
        else:
            wrapped = textwrap.fill(
                description,
                width=max_width,
                initial_indent=prefix + '"""',
                subsequent_indent=prefix,
            )
            lines.append(wrapped)
    else:
        lines.append(f'{prefix}"""')

    if description and (params or return_type):
        lines.append("")

    for pname, pdesc in params:
        if not pdesc:
            pdesc = pname.replace("_", " ")
        pdesc = pdesc[0].upper() + pdesc[1:] if pdesc else pdesc
        pdesc = pdesc.rstrip()
        if not pdesc.endswith("."):
            pdesc += "."
        param_line = f":param {pname}: {pdesc}"
        wrapped = textwrap.fill(
            param_line,
            width=max_width,
            subsequent_indent="    ",
        )
        lines.extend(f"{prefix}{line}" for line in wrapped.splitlines())

    if return_type:
        lines.append(f"{prefix}:return: {return_type}")

    lines.append(f'{prefix}"""')
    return lines


def _param_value_expr(param: dict, py_name: str) -> str:
    """Build the expression producing a parameter's wire value.

    Array parameters declared with ``explode: false`` are joined into a
    comma-separated string: the API rejects them as repeated query keys.

    :param param: resolved parameter dict.
    :param py_name: Python name of the method argument.
    :return: expression string.
    """
    schema = param.get("schema") or {}
    if schema.get("type") == "array" and param.get("explode") is False:
        if param.get("required", False):
            return f'",".join({py_name})'
        return f'",".join({py_name}) if {py_name} else None'
    return py_name


def _build_dict_literal(
    params: list[dict],
    param_map: dict[str, str],
    var_name: str,
) -> list[str]:
    """Build a dict literal assignment from API parameters.

    :param params: list of resolved parameter dicts.
    :param param_map: mapping of API name to Python name.
    :param var_name: variable name for the assignment.
    :return: list of code lines.
    """
    if not params:
        return []
    if len(params) == 1:
        api_name = params[0]["name"]
        py_name = param_map[api_name]
        return [f'        {var_name} = {{"{api_name}": {_param_value_expr(params[0], py_name)}}}']
    lines = [f"        {var_name} = {{"]
    for p in params:
        api_name = p["name"]
        py_name = param_map[api_name]
        lines.append(f'            "{api_name}": {_param_value_expr(p, py_name)},')
    lines.append("        }")
    return lines


def _generate_method(
    path: str,
    http_method: str,
    operation: dict,
    spec: dict,
    tag: str,
    overrides: dict[str, str],
) -> tuple[str, set[str]]:
    """Generate a single async method.

    :param path: API path string.
    :param http_method: HTTP method (get, post, etc.).
    :param operation: OpenAPI operation dictionary.
    :param spec: full OpenAPI spec.
    :param tag: API tag.
    :param overrides: method name overrides.
    :return: tuple of ``(code_string, model_imports_set)``.
    """
    operation_id = operation.get("operationId", "unknown")
    method_name = operation_to_method_name(operation_id, tag, overrides)
    description = operation.get("description", "")

    raw_params = operation.get("parameters", [])
    params = [resolve_parameter(p, spec) for p in raw_params]

    path_params = [p for p in params if p.get("in") == "path"]
    query_params = [p for p in params if p.get("in") == "query"]
    header_params = [p for p in params if p.get("in") == "header"]

    body_schema = resolve_request_body(operation, spec)
    body_schema_ref = None
    body_is_raw = False
    if body_schema is not None:
        if "$ref" in body_schema:
            body_schema_ref = ref_name(body_schema["$ref"])
        elif body_schema.get("type") == "object" and "properties" in body_schema:
            body_is_raw = True

    response_type = resolve_response_type(operation, spec)
    model_imports: set[str] = set()
    if response_type and response_type not in NON_MODEL_TYPES:
        model_imports.add(response_type)

    sig_params = ["self"]
    path_param_map: dict[str, str] = {}
    query_param_map: dict[str, str] = {}
    header_param_map: dict[str, str] = {}

    for p in path_params:
        api_name = p["name"]
        py_name = to_python_name(api_name)
        path_param_map[api_name] = py_name
        ptype = param_python_type(p.get("schema", {}))
        sig_params.append(f"{py_name}: {ptype}")

    if body_schema_ref:
        model_imports.add(body_schema_ref)
        sig_params.append(f"body: {body_schema_ref}")
    elif body_is_raw:
        sig_params.append("body: dict[str, t.Any]")

    required_query: list[str] = []
    optional_query: list[str] = []
    for p in query_params:
        api_name = p["name"]
        py_name = to_python_name(api_name)
        query_param_map[api_name] = py_name
        ptype = param_python_type(p.get("schema", {}))
        required = p.get("required", False)
        default = param_default(p)

        if required and default is None:
            required_query.append(f"{py_name}: {ptype}")
        else:
            default_val = default if default is not None else "None"
            if default is None:
                ptype = f"{ptype} | None"
            optional_query.append(f"{py_name}: {ptype} = {default_val}")

    sig_params.extend(required_query)
    sig_params.extend(optional_query)

    for p in header_params:
        api_name = p["name"]
        py_name = to_python_name(api_name)
        header_param_map[api_name] = py_name
        ptype = param_python_type(p.get("schema", {}))
        sig_params.append(f"{py_name}: {ptype} | None = None")

    if response_type == "dict[str, t.Any]":  # noqa: SIM108
        return_type_str = "t.Any"
    else:
        return_type_str = response_type if response_type else "None"

    lines: list[str] = []
    sig = ", ".join(sig_params) + ","
    lines.append(f"    async def {method_name}({sig}) -> {return_type_str}:")

    doc_params: list[tuple[str, str]] = []
    for p in path_params:
        py_name = path_param_map[p["name"]]
        doc_params.append((py_name, p.get("description", "")))
    if body_schema_ref or body_is_raw:
        doc_params.append(("body", "Request body."))
    for p in query_params:
        py_name = query_param_map[p["name"]]
        doc_params.append((py_name, p.get("description", "")))
    for p in header_params:
        py_name = header_param_map[p["name"]]
        doc_params.append((py_name, p.get("description", "")))

    lines.extend(_format_docstring(description, doc_params, response_type))

    has_path_params = "{" in path
    if has_path_params:
        fmt_path = path
        for api_name, py_name in path_param_map.items():
            fmt_path = fmt_path.replace(
                "{" + api_name + "}",
                "{" + py_name + "}",
            )
        lines.append(f'        path = f"{fmt_path}"')
    else:
        lines.append(f'        path = "{path}"')

    lines.extend(_build_dict_literal(query_params, query_param_map, "params"))
    lines.extend(_build_dict_literal(header_params, header_param_map, "headers"))

    req_parts = [f'            method="{http_method.upper()}",']
    req_parts.append("            path=path,")
    if query_params:
        req_parts.append("            params=params,")
    if body_schema_ref:
        req_parts.append("            body=body.model_dump(by_alias=True, exclude_none=True),")
    elif body_is_raw:
        req_parts.append("            body=body,")
    if header_params:
        req_parts.append("            headers=headers,")
    if response_type and response_type != "dict[str, t.Any]":
        req_parts.append(f"            response_model={response_type},")

    if return_type_str == "None":
        lines.append("        await self._request(")
    else:
        lines.append("        return await self._request(")
    lines.extend(req_parts)
    lines.append("        )")

    return "\n".join(lines), model_imports


def run() -> None:
    """Generate all resource files."""
    spec = load_spec()
    overrides = load_config().get("method_names", {})
    tag_endpoints = group_endpoints_by_tag(spec)

    total = sum(len(v) for v in tag_endpoints.values())
    print(f"Found {total} endpoints across {len(tag_endpoints)} tags")

    RESOURCES_DIR.mkdir(parents=True, exist_ok=True)

    modules: list[tuple[str, str]] = []

    for tag in sorted(tag_endpoints):
        endpoints = tag_endpoints[tag]
        module = tag_to_module_name(tag)
        class_name = tag_to_class_name(tag)
        all_model_imports: set[str] = set()
        methods = []

        for path, http_method, operation in endpoints:
            code, imports = _generate_method(
                path,
                http_method,
                operation,
                spec,
                tag,
                overrides,
            )
            methods.append({"code": code})
            all_model_imports |= imports

        template = env.get_template("resource.py.j2")
        result = template.render(
            class_name=class_name,
            model_imports=all_model_imports,
            methods=methods,
        )
        (RESOURCES_DIR / f"{module}.py").write_text(result)
        print(f"Generated {module}.py ({len(endpoints)} methods)")
        modules.append((module, class_name))

    # _base.py
    base_template = env.get_template("resource_base.py.j2")
    (RESOURCES_DIR / "_base.py").write_text(base_template.render())
    print("Generated _base.py")

    # __init__.py
    all_names = [f'"{cn}"' for _, cn in modules]
    template = env.get_template("resource_init.py.j2")
    result = template.render(modules=modules, all_names=all_names)
    (RESOURCES_DIR / "__init__.py").write_text(result)
    print("Generated __init__.py")

    # mixin.py
    template = env.get_template("mixin.py.j2")
    result = template.render(modules=modules)
    (RESOURCES_DIR.parent / "mixin.py").write_text(result)
    print("Generated mixin.py")

    print(f"\nDone! Generated {len(modules)} resource modules.")
    run_ruff(RESOURCES_DIR)
    run_ruff(RESOURCES_DIR.parent / "mixin.py")

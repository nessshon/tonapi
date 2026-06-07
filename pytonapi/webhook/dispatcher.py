from __future__ import annotations

import inspect
import typing as t
from urllib.parse import urlparse

from pydantic import TypeAdapter

from pytonapi.exceptions import TONAPIError
from pytonapi.webhook.models import (
    AccountTxEvent,
    MempoolMsgEvent,
    NewContractsEvent,
    OpcodeMsgEvent,
    WebhookEventType,
)

if t.TYPE_CHECKING:
    from pytonapi.webhook.client import TonapiWebhookClient

_EVENT_TYPES: dict[WebhookEventType, type] = {
    WebhookEventType.ACCOUNT_TX: AccountTxEvent,
    WebhookEventType.MEMPOOL_MSG: MempoolMsgEvent,
    WebhookEventType.OPCODE_MSG: OpcodeMsgEvent,
    WebhookEventType.NEW_CONTRACTS: NewContractsEvent,
}

_ADAPTERS: dict[WebhookEventType, TypeAdapter[t.Any]] = {key: TypeAdapter(cls) for key, cls in _EVENT_TYPES.items()}


class TonapiWebhookDispatcher:
    """Path-based event dispatcher for incoming webhook notifications."""

    DEFAULT_SUFFIXES: t.ClassVar[dict[WebhookEventType, str]] = {
        WebhookEventType.ACCOUNT_TX: "/account-tx",
        WebhookEventType.MEMPOOL_MSG: "/mempool-msg",
        WebhookEventType.OPCODE_MSG: "/opcode-msg",
        WebhookEventType.NEW_CONTRACTS: "/new-contracts",
    }

    def __init__(
        self,
        url: str = "",
        *,
        client: TonapiWebhookClient | None = None,
        accounts: list[str] | None = None,
        opcodes: list[str] | None = None,
        **kwargs: t.Any,
    ) -> None:
        """Initialize the webhook dispatcher.

        :param url: Public webhook URL prefix. Suffixes like ``/account-tx``
            are appended automatically for each event type.
        :param client: ``TonapiWebhookClient`` instance used for webhook
            CRUD and subscriptions. Required only for ``setup()`` / ``teardown()``.
        :param accounts: Account IDs to subscribe to.
        :param opcodes: Opcodes to subscribe to.
        :param kwargs: Default dependencies injected into every handler call.
            Values passed to ``process()`` take priority over these defaults.
        """
        self._client = client
        self._url = url.rstrip("/")
        self._path = urlparse(self._url).path
        self._accounts: set[str] = set(accounts) if accounts else set()
        self._opcodes: set[str] = set(opcodes) if opcodes else set()
        self._defaults: dict[str, t.Any] = kwargs

        # path -> secret token (populated by setup)
        self._tokens: dict[str, str] = {}

        # event_type -> list of (account_filter, handler, path)
        self._handlers: dict[
            WebhookEventType,
            list[tuple[frozenset[str] | None, t.Callable[..., t.Any], str]],
        ] = {et: [] for et in WebhookEventType}

        # path -> event_type (built lazily on first process call)
        self._path_map: dict[str, WebhookEventType] | None = None

    @property
    def url(self) -> str:
        """Public webhook URL prefix."""
        return self._url

    @property
    def accounts(self) -> frozenset[str]:
        """Account IDs to subscribe to."""
        return frozenset(self._accounts)

    @property
    def opcodes(self) -> frozenset[str]:
        """Opcodes to subscribe to."""
        return frozenset(self._opcodes)

    async def setup(self) -> None:
        """Open session, create webhooks, subscribe, and store tokens.

        For each event type with registered handlers, creates (or reuses)
        a separate TONAPI webhook and subscribes it according to the
        dispatcher config. Secret tokens are stored automatically.
        """
        if self._client is None:
            raise TONAPIError("client is required for setup()")
        await self._client.create_session()

        for event_type, handlers in self._handlers.items():
            if not handlers:
                continue
            # One webhook per distinct path (incl. custom ``path=``) so every
            # path gets its token stored — otherwise auth is silently skipped.
            for local_path in sorted({path for _, _, path in handlers}):
                webhook = await self._client.ensure(self._endpoint_for_path(local_path))
                self._tokens[local_path] = webhook.token

                if event_type is WebhookEventType.ACCOUNT_TX and self._accounts:
                    await webhook.sync_accounts(list(self._accounts))
                elif event_type is WebhookEventType.MEMPOOL_MSG:
                    await webhook.subscribe_mempool_msg()
                elif event_type is WebhookEventType.OPCODE_MSG and self._opcodes:
                    for opcode in self._opcodes:
                        await webhook.subscribe_opcode_msg(opcode)
                elif event_type is WebhookEventType.NEW_CONTRACTS:
                    await webhook.subscribe_new_contracts()

    async def teardown(self, cleanup: bool = False) -> None:
        """Close session and optionally unsubscribe.

        :param cleanup: When ``True``, unsubscribe from all events
            before closing the session. Default ``False`` — subscriptions
            persist across restarts.
        """
        if self._client is None:
            raise TONAPIError("client is required for teardown()")

        if cleanup:
            from pytonapi.webhook.client import TonapiWebhook

            webhooks = await self._client.list()
            endpoint_map = {w.endpoint: w for w in webhooks}

            for event_type, handlers in self._handlers.items():
                if not handlers:
                    continue
                for local_path in sorted({path for _, _, path in handlers}):
                    endpoint = self._endpoint_for_path(local_path)
                    info = endpoint_map.get(endpoint)
                    if info is None:
                        continue
                    webhook = TonapiWebhook(self._client, info.id, info.endpoint, info.token)

                    if event_type is WebhookEventType.ACCOUNT_TX and self._accounts:
                        await webhook.unsubscribe(list(self._accounts))
                    elif event_type is WebhookEventType.MEMPOOL_MSG:
                        await webhook.unsubscribe_mempool_msg()
                    elif event_type is WebhookEventType.OPCODE_MSG and self._opcodes:
                        for opcode in self._opcodes:
                            await webhook.unsubscribe_opcode_msg(opcode)
                    elif event_type is WebhookEventType.NEW_CONTRACTS:
                        await webhook.unsubscribe_new_contracts()

        await self._client.close_session()

    @property
    def paths(self) -> dict[WebhookEventType, str]:
        """Mapping of event types to their resolved paths.

        Only includes event types that have at least one handler registered.

        :return: Event type to path mapping.
        """
        return {et: handlers[0][2] for et, handlers in self._handlers.items() if handlers}

    def _resolve_path(self, event_type: WebhookEventType) -> str:
        """Build the local path for an event type.

        :param event_type: Webhook event type.
        :return: URL path component for routing.
        """
        return self._path + self.DEFAULT_SUFFIXES[event_type]

    def _endpoint_for_path(self, path: str) -> str:
        """Build the absolute webhook endpoint URL for a local path.

        :param path: Local URL path component.
        :return: Absolute endpoint URL.
        """
        parsed = urlparse(self._url)
        return parsed._replace(path=path, params="", query="", fragment="").geturl()

    def _build_path_map(self) -> dict[str, WebhookEventType]:
        """Build reverse mapping from every registered path to its event type."""
        return {path: et for et, handlers in self._handlers.items() for _, _, path in handlers}

    def account_tx(
        self,
        *accounts: str,
        path: str | None = None,
    ) -> t.Callable[[t.Callable[..., t.Any]], t.Callable[..., t.Any]]:
        """Register a handler for account transaction events.

        :param accounts: Account IDs to filter by. When empty,
            the handler receives all account transaction events.
        :param path: Custom URL path, or ``None`` for default.
        :return: Decorator that registers the handler.
        """
        return self._make_decorator(WebhookEventType.ACCOUNT_TX, accounts, path)

    def mempool_msg(
        self,
        *,
        path: str | None = None,
    ) -> t.Callable[[t.Callable[..., t.Any]], t.Callable[..., t.Any]]:
        """Register a handler for mempool message events.

        :param path: Custom URL path, or ``None`` for default.
        :return: Decorator that registers the handler.
        """
        return self._make_decorator(WebhookEventType.MEMPOOL_MSG, (), path)

    def opcode_msg(
        self,
        *accounts: str,
        path: str | None = None,
    ) -> t.Callable[[t.Callable[..., t.Any]], t.Callable[..., t.Any]]:
        """Register a handler for opcode subscription events.

        :param accounts: Account IDs to filter by. When empty,
            the handler receives all opcode events.
        :param path: Custom URL path, or ``None`` for default.
        :return: Decorator that registers the handler.
        """
        return self._make_decorator(WebhookEventType.OPCODE_MSG, accounts, path)

    def new_contracts(
        self,
        *accounts: str,
        path: str | None = None,
    ) -> t.Callable[[t.Callable[..., t.Any]], t.Callable[..., t.Any]]:
        """Register a handler for new contract deployment events.

        :param accounts: Account IDs to filter by. When empty,
            the handler receives all new contract events.
        :param path: Custom URL path, or ``None`` for default.
        :return: Decorator that registers the handler.
        """
        return self._make_decorator(WebhookEventType.NEW_CONTRACTS, accounts, path)

    def register(
        self,
        event_type: WebhookEventType,
        handler: t.Callable[..., t.Any],
        *accounts: str,
        path: str | None = None,
    ) -> None:
        """Register a handler without using a decorator.

        :param event_type: Webhook event type.
        :param handler: Callable to invoke on matching events.
        :param accounts: Account IDs to filter by.
        :param path: Custom URL path for this event type.
        :raises ValueError: If ``event_type`` is not recognized.
        """
        if event_type not in _EVENT_TYPES:
            raise ValueError(
                f"Unknown event type {event_type!r}. Expected one of: {', '.join(et.value for et in WebhookEventType)}"
            )
        account_filter = frozenset(accounts) if accounts else None
        resolved_path = path or self._resolve_path(event_type)
        self._handlers[event_type].append((account_filter, handler, resolved_path))
        self._path_map = None

    async def process(
        self,
        path: str,
        data: dict[str, t.Any],
        *,
        authorization: str | None = None,
        **kwargs: t.Any,
    ) -> None:
        """Parse an incoming event and dispatch to matching handlers.

        :param path: URL path of the incoming request.
        :param data: Raw webhook payload dictionary.
        :param authorization: Value of the ``Authorization`` header.
        :param kwargs: Per-request dependencies.
        :raises TONAPIError: If the secret token is invalid or the
            path is not recognized.
        """
        if self._path_map is None:
            self._path_map = self._build_path_map()

        event_type = self._path_map.get(path)
        if event_type is None:
            raise TONAPIError(f"Unknown webhook path: {path}")

        expected_token = self._tokens.get(path)
        if expected_token is not None and authorization != f"Bearer {expected_token}":
            raise TONAPIError("Invalid webhook token")

        adapter = _ADAPTERS[event_type]
        event = adapter.validate_python(data)
        merged = {**self._defaults, **kwargs}

        for account_filter, handler, _ in self._handlers[event_type]:
            if account_filter is not None and hasattr(event, "account_id") and event.account_id not in account_filter:
                continue
            await self._call_handler(handler, event, merged)

    @staticmethod
    async def _call_handler(
        handler: t.Callable[..., t.Any],
        event: t.Any,
        dependencies: dict[str, t.Any],
    ) -> None:
        """Call a handler, injecting only the parameters it accepts.

        :param handler: Handler callable.
        :param event: Parsed webhook event.
        :param dependencies: Available keyword arguments.
        """
        sig = inspect.signature(handler)
        inject: dict[str, t.Any] = {}
        first = True
        for name in sig.parameters:
            if first:
                inject[name] = event
                first = False
            elif name in dependencies:
                inject[name] = dependencies[name]

        result = handler(**inject)
        if inspect.isawaitable(result):
            await result

    def _make_decorator(
        self,
        event_type: WebhookEventType,
        accounts: tuple[str, ...],
        path: str | None,
    ) -> t.Callable[[t.Callable[..., t.Any]], t.Callable[..., t.Any]]:
        """Create a decorator for registering event handlers.

        :param event_type: Webhook event type.
        :param accounts: Account IDs to filter by.
        :param path: Custom URL path or ``None`` for default.
        :return: Decorator function.
        """
        account_filter = frozenset(accounts) if accounts else None
        resolved_path = path or self._resolve_path(event_type)

        def decorator(fn: t.Callable[..., t.Any]) -> t.Callable[..., t.Any]:
            self._handlers[event_type].append((account_filter, fn, resolved_path))
            self._path_map = None
            return fn

        return decorator

# Jettons

6 methods from `tonapi.jettons`:

## get_jettons

Get list of jettons.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| limit | int | no | 100 | Max results |
| offset | int | no | 0 | Pagination offset (deprecated, prefer `last_account_id`) |
| last_account_id | str \| None | no | None | Cursor: `metadata.address` of the last jetton from the previous page |

Returns: `Jettons`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py jettons get_jettons --limit 10
```

```python
result = await tonapi.jettons.get_jettons(limit=10)
```

## get_jetton_info

Get jetton metadata and info.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Jetton master address |

Returns: `JettonInfo`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py jettons get_jetton_info --account-id EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs
```

```python
result = await tonapi.jettons.get_jetton_info("EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs")
```

## get_jetton_infos_by_addresses

Get multiple jettons info in bulk.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| body | dict | yes | — | Request body with `account_ids` list |

Returns: `Jettons`

```python
result = await tonapi.jettons.get_jetton_infos_by_addresses(body={"account_ids": ["EQ..."]})
```

## get_jetton_holders

Get jetton holders.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Jetton master address |
| limit | int | no | 1000 | Max results |
| offset | int | no | 0 | Pagination offset (only with `sort_by="balance"`, up to 9000 rows) |
| sort_by | str | no | "balance" | Sort: "balance" (top holders) or "address" (cursor pagination) |
| last_account_id | str \| None | no | None | Cursor for `sort_by="address"`: `address` of the last holder, not `owner.address` |

Returns: `JettonHolders`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py jettons get_jetton_holders --account-id EQ... --limit 10
```

```python
result = await tonapi.jettons.get_jetton_holders("EQ...", limit=10)
```

## get_jetton_transfer_payload

Get jetton transfer payload for a specific account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Destination account address |
| jetton_id | str | yes | — | Jetton master address |

Returns: `JettonTransferPayload`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py jettons get_jetton_transfer_payload --account-id EQ... --jetton-id EQ...
```

```python
result = await tonapi.jettons.get_jetton_transfer_payload("EQ...", "EQ...")
```

## get_events

Get jetton-related events.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| event_id | str | yes | — | Event ID |
| accept_language | str \| None | no | None | Language for localized content |

Returns: `Event`

```python
result = await tonapi.jettons.get_events("event_id")
```

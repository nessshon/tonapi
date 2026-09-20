# Migration

2 methods from `tonapi.migration`:

## get_wallets

Get migratable assets value (TON balance, jettons with prices, NFT count) for several wallets.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| body | dict | yes | — | Request body with `account_ids` list |
| currencies | list[str] \| None | no | None | Currencies for price conversion |

Returns: `MigrationWallets`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py migration get_wallets --body '{"account_ids":["EQ..."]}'
```

```python
result = await tonapi.migration.get_wallets(body={"account_ids": ["EQ..."]}, currencies=["usd"])
```

## prepare_migration

Prepare ordered signable transactions that migrate every asset from `from` to `to` (409 when the source can't cover gas).

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| body | MigrationPrepareRequest | yes | — | Request body model with `from`, `to` and optional gas fields |

Returns: `MigrationPrepareResponse`

```python
from pytonapi.rest.models import MigrationPrepareRequest

body = MigrationPrepareRequest.model_validate({"from": "EQ...", "to": "EQ..."})
result = await tonapi.migration.prepare_migration(body=body)
```

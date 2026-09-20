# Accounts

22 methods from `tonapi.accounts`:

## get_accounts

Get multiple accounts info in bulk.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| body | dict | yes | — | Request body with `account_ids` list |
| currency | str \| None | no | None | Currency for balance conversion |

Returns: `Accounts`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_accounts --body '{"account_ids":["EQ...","EQ..."]}'
```

```python
result = await tonapi.accounts.get_accounts(body={"account_ids": ["EQ..."]})
```

## get_account

Get full account information.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `Account`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account --account-id EQDtFpEwcFAEcRe5mLVh2N6C0x-_hJEM7W61_JLnSF74p4q2
```

```python
result = await tonapi.accounts.get_account("EQDtFpEwcFAEcRe5mLVh2N6C0x-_hJEM7W61_JLnSF74p4q2")
```

## account_dns_back_resolve

Get DNS names associated with account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `DomainNames`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts account_dns_back_resolve --account-id EQ...
```

```python
result = await tonapi.accounts.account_dns_back_resolve("EQ...")
```

## get_account_jettons_balances

Get jetton balances for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| currencies | list[str] \| None | no | None | Currencies for balance conversion |
| supported_extensions | list[str] \| None | no | None | Supported jetton extensions filter (`["defi"]` adds `defi_asset` to balances) |
| limit | int | no | 1000 | Max results |
| offset | int | no | 0 | Pagination offset |

Returns: `JettonsBalances`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_jettons_balances --account-id EQ... --limit 10
```

```python
result = await tonapi.accounts.get_account_jettons_balances("EQ...", limit=10)
```

## get_account_jetton_balance

Get single jetton balance for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| jetton_id | str | yes | — | Jetton master address |
| currencies | list[str] \| None | no | None | Currencies for balance conversion |
| supported_extensions | list[str] \| None | no | None | Supported jetton extensions filter (`["defi"]` adds `defi_asset` to balances) |

Returns: `JettonBalance`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_jetton_balance --account-id EQ... --jetton-id EQ...
```

```python
result = await tonapi.accounts.get_account_jetton_balance("EQ...", "EQ...")
```

## get_account_jettons_history

Get all jetton operations history for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| limit | int | yes | — | Max results |
| before_lt | int \| None | no | None | Cursor for pagination |

Returns: `JettonOperations`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_jettons_history --account-id EQ... --limit 10
```

```python
result = await tonapi.accounts.get_account_jettons_history("EQ...", limit=10)
```

## get_account_jetton_history_by_id

Get jetton operations history for a specific jetton.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| jetton_id | str | yes | — | Jetton master address |
| limit | int | yes | — | Max results |
| before_lt | int \| None | no | None | Cursor for pagination |
| start_date | int \| None | no | None | Start date (Unix timestamp) |
| end_date | int \| None | no | None | End date (Unix timestamp) |
| accept_language | str \| None | no | None | Language for localized content |

Returns: `AccountEvents`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_jetton_history_by_id --account-id EQ... --jetton-id EQ... --limit 10
```

```python
result = await tonapi.accounts.get_account_jetton_history_by_id("EQ...", "EQ...", limit=10)
```

## get_account_nft_items

Get NFT items owned by an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| collection | str \| None | no | None | Filter by NFT collection address |
| limit | int | no | 1000 | Max results |
| offset | int | no | 0 | Pagination offset |
| indirect_ownership | bool | no | False | Include indirectly owned NFTs |

Returns: `NftItems`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_nft_items --account-id EQ... --limit 10
```

```python
result = await tonapi.accounts.get_account_nft_items("EQ...", limit=10)
```

## get_account_events

Get account events (parsed actions).

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| limit | int | yes | — | Max results |
| initiator | bool | no | False | Only events initiated by this account |
| subject_only | bool | no | False | Only events where account is subject |
| after_lt | int \| None | no | None | Events after this logical time |
| before_lt | int \| None | no | None | Events before this logical time |
| start_date | int \| None | no | None | Start date (Unix timestamp) |
| end_date | int \| None | no | None | End date (Unix timestamp) |
| sort_order | str | no | "desc" | Sort: "asc" or "desc" |
| accept_language | str \| None | no | None | Language for localized content |

Returns: `AccountEvents`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_events --account-id EQ... --limit 10
```

```python
result = await tonapi.accounts.get_account_events("EQ...", limit=10)
```

## get_account_event

Get a specific event for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| event_id | str | yes | — | Event ID |
| subject_only | bool | no | False | Only if account is subject |
| accept_language | str \| None | no | None | Language for localized content |

Returns: `AccountEvent`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_event --account-id EQ... --event-id ...
```

```python
result = await tonapi.accounts.get_account_event("EQ...", "event_id")
```

## get_account_traces

Get account traces.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| before_lt | int \| None | no | None | Cursor for pagination |
| limit | int | no | 100 | Max results |

Returns: `TraceIDs`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_traces --account-id EQ... --limit 10
```

```python
result = await tonapi.accounts.get_account_traces("EQ...", limit=10)
```

## get_account_subscriptions

Get account subscriptions.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `Subscriptions`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_subscriptions --account-id EQ...
```

```python
result = await tonapi.accounts.get_account_subscriptions("EQ...")
```

## reindex_account

Trigger reindexing for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `None`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts reindex_account --account-id EQ...
```

```python
await tonapi.accounts.reindex_account("EQ...")
```

## search_accounts

Search accounts by name.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| name | str | yes | — | Search query |

Returns: `FoundAccounts`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts search_accounts --name "wallet"
```

```python
result = await tonapi.accounts.search_accounts("wallet")
```

## get_account_dns_expiring

Get expiring DNS domains for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| period | int \| None | no | None | Period in seconds to check |

Returns: `DnsExpiring`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_dns_expiring --account-id EQ...
```

```python
result = await tonapi.accounts.get_account_dns_expiring("EQ...")
```

## get_account_public_key

Get public key for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `dict[str, Any]`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_public_key --account-id EQ...
```

```python
result = await tonapi.accounts.get_account_public_key("EQ...")
```

## get_account_multisigs

Get multisig wallets for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `Multisigs`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_multisigs --account-id EQ...
```

```python
result = await tonapi.accounts.get_account_multisigs("EQ...")
```

## get_account_diff

Get account balance diff between two dates.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| start_date | int | yes | — | Start date (Unix timestamp) |
| end_date | int | yes | — | End date (Unix timestamp) |

Returns: `dict[str, Any]`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_diff --account-id EQ... --start-date 1700000000 --end-date 1700100000
```

```python
result = await tonapi.accounts.get_account_diff("EQ...", start_date=1700000000, end_date=1700100000)
```

## get_account_defi_assets

Get DeFi assets locked in custom smart contracts (TON Whales staking, EVAA lending positions).

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `DefiAssets`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py accounts get_account_defi_assets --account-id EQ...
```

```python
result = await tonapi.accounts.get_account_defi_assets("EQ...")
```

## get_account_extra_currency_history_by_id

Get extra currency history for an account.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| id | int | yes | — | Extra currency ID |
| limit | int | yes | — | Max results |
| before_lt | int \| None | no | None | Cursor for pagination |
| start_date | int \| None | no | None | Start date (Unix timestamp) |
| end_date | int \| None | no | None | End date (Unix timestamp) |
| accept_language | str \| None | no | None | Language for localized content |

Returns: `AccountEvents`

```python
result = await tonapi.accounts.get_account_extra_currency_history_by_id("EQ...", id=1, limit=10)
```

## get_jetton_account_history_by_id

Get jetton operations for a specific account and jetton (via jetton path).

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| jetton_id | str | yes | — | Jetton master address |
| limit | int | yes | — | Max results |
| before_lt | int \| None | no | None | Cursor for pagination |
| start_date | int \| None | no | None | Start date (Unix timestamp) |
| end_date | int \| None | no | None | End date (Unix timestamp) |

Returns: `JettonOperations`

```python
result = await tonapi.accounts.get_jetton_account_history_by_id("EQ...", "EQ...", limit=10)
```

## emulate_message_to_account_event

Emulate a message and get the resulting account event.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| body | dict | yes | — | Message body (BOC) |
| ignore_signature_check | bool \| None | no | None | Ignore signature verification |
| accept_language | str \| None | no | None | Language for localized content |

Returns: `AccountEvent`

```python
result = await tonapi.accounts.emulate_message_to_account_event("EQ...", body={"boc": "..."})
```

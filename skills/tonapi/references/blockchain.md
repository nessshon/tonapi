# Blockchain

23 methods from `tonapi.blockchain`:

## get_reduced_blockchain_blocks

Get reduced blockchain blocks.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| from_ | int | yes | — | Start block seqno |
| to | int | yes | — | End block seqno |

Returns: `ReducedBlocks`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_reduced_blockchain_blocks --from_ 1000 --to 1010
```

```python
result = await tonapi.blockchain.get_reduced_blockchain_blocks(from_=1000, to=1010)
```

## get_block

Get block by ID.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| block_id | str | yes | — | Block ID |

Returns: `BlockchainBlock`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_block --block-id ...
```

```python
result = await tonapi.blockchain.get_block("block_id")
```

## download_blockchain_block_boc

Download block BOC.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| block_id | str | yes | — | Block ID |

Returns: `bytes`

```python
result = await tonapi.blockchain.download_blockchain_block_boc("block_id")
```

## get_masterchain_shards

Get masterchain shards.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| masterchain_seqno | int | yes | — | Masterchain block seqno |

Returns: `BlockchainBlockShards`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_masterchain_shards --masterchain-seqno 12345
```

```python
result = await tonapi.blockchain.get_masterchain_shards(12345)
```

## get_masterchain_blocks

Get masterchain blocks.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| masterchain_seqno | int | yes | — | Masterchain block seqno |

Returns: `BlockchainBlocks`

```python
result = await tonapi.blockchain.get_masterchain_blocks(12345)
```

## get_masterchain_transactions

Get masterchain transactions.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| masterchain_seqno | int | yes | — | Masterchain block seqno |
| offset | int | no | 0 | Pagination offset |
| limit | int \| None | no | None | Max results |

Returns: `Transactions`

```python
result = await tonapi.blockchain.get_masterchain_transactions(12345, limit=100)
```

## get_config_from_block

Get blockchain config from a specific block.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| masterchain_seqno | int | yes | — | Masterchain block seqno |

Returns: `BlockchainConfig`

```python
result = await tonapi.blockchain.get_config_from_block(12345)
```

## get_raw_blockchain_config_from_block

Get raw blockchain config from a specific block.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| masterchain_seqno | int | yes | — | Masterchain block seqno |

Returns: `RawBlockchainConfig`

```python
result = await tonapi.blockchain.get_raw_blockchain_config_from_block(12345)
```

## get_block_transactions

Get transactions in a block.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| block_id | str | yes | — | Block ID |

Returns: `Transactions`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_block_transactions --block-id ...
```

```python
result = await tonapi.blockchain.get_block_transactions("block_id")
```

## get_transaction

Get transaction by ID.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| transaction_id | str | yes | — | Transaction ID (hash) |

Returns: `Transaction`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_transaction --transaction-id ...
```

```python
result = await tonapi.blockchain.get_transaction("tx_hash")
```

## get_transaction_by_message_hash

Get transaction by message hash.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| msg_id | str | yes | — | Message hash |

Returns: `Transaction`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_transaction_by_message_hash --msg-id ...
```

```python
result = await tonapi.blockchain.get_transaction_by_message_hash("msg_hash")
```

## get_validators

Get current validators.

Returns: `Validators`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_validators
```

```python
result = await tonapi.blockchain.get_validators()
```

## get_masterchain_head

Get the latest masterchain block.

Returns: `BlockchainBlock`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_masterchain_head
```

```python
result = await tonapi.blockchain.get_masterchain_head()
```

## get_raw_account

Get raw account data from blockchain.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `BlockchainRawAccount`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_raw_account --account-id EQ...
```

```python
result = await tonapi.blockchain.get_raw_account("EQ...")
```

## get_raw_accounts

Get raw data for several accounts from blockchain.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| body | dict | yes | — | Request body with `account_ids` list |

Returns: `BlockchainRawAccounts`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_raw_accounts --body '{"account_ids":["EQ...","EQ..."]}'
```

```python
result = await tonapi.blockchain.get_raw_accounts(body={"account_ids": ["EQ...", "EQ..."]})
```

## get_account_transactions

Get account transactions from blockchain.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |
| after_lt | int \| None | no | None | Transactions after this logical time |
| before_lt | int \| None | no | None | Transactions before this logical time |
| limit | int | no | 100 | Max results |
| sort_order | str | no | "desc" | Sort: "asc" or "desc" |

Returns: `Transactions`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_account_transactions --account-id EQ... --limit 10
```

```python
result = await tonapi.blockchain.get_account_transactions("EQ...", limit=10)
```

## execute_get_method

Execute a smart contract get-method.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Contract address in any form |
| method_name | str | yes | — | Get-method name |
| args | list[str] \| None | no | None | Method arguments |

Returns: `MethodExecutionResult`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain execute_get_method --account-id EQ... --method-name get_wallet_data
```

```python
result = await tonapi.blockchain.execute_get_method("EQ...", "get_wallet_data")
```

## execute_get_method_with_body

Execute a smart contract get-method with body.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Contract address |
| method_name | str | yes | — | Get-method name |
| body | dict | yes | — | Request body with method args |

Returns: `MethodExecutionResult`

```python
result = await tonapi.blockchain.execute_get_method_with_body("EQ...", "method", body={...})
```

## send_message

Send a signed message (BOC) to the blockchain.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| body | dict | yes | — | Request body with `boc` field |

Returns: `None`

```python
await tonapi.blockchain.send_message(body={"boc": "base64_encoded_boc"})
```

## get_config

Get current blockchain config.

Returns: `BlockchainConfig`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain get_config
```

```python
result = await tonapi.blockchain.get_config()
```

## get_raw_blockchain_config

Get current raw blockchain config.

Returns: `RawBlockchainConfig`

```python
result = await tonapi.blockchain.get_raw_blockchain_config()
```

## account_inspect

Inspect account contract code.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| account_id | str | yes | — | Account address in any form |

Returns: `BlockchainAccountInspect`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py blockchain account_inspect --account-id EQ...
```

```python
result = await tonapi.blockchain.account_inspect("EQ...")
```

## get_library_by_hash

Get smart contract library by hash.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| hash | str | yes | — | Library hash |

Returns: `BlockchainLibrary`

```python
result = await tonapi.blockchain.get_library_by_hash("hash")
```

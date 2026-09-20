---
name: tonapi
description: >
  Work with TON blockchain via the tonapi Python SDK — query accounts,
  transactions, jettons, NFTs, staking, validator rewards, DNS, prepare wallet
  migration, emulate messages, subscribe to
  real-time events, and manage webhooks. Use this skill whenever the user
  mentions TONAPI, tonapi.io, TON blockchain data, wallet balance, jetton
  transfers, NFT collections, or wants to interact with TON via TONAPI.
  Also use when the user works with code that imports from pytonapi.rest,
  pytonapi.streaming, pytonapi.webhook, or pytonapi.types, or asks about
  TONAPI endpoints, even if they don't explicitly mention "pytonapi".
---

Python SDK for querying TON blockchain via TONAPI. Covers REST API, streaming (SSE/WebSocket), and webhooks with event
dispatcher. Read the relevant reference file, then either execute via runner or generate SDK code.

## API Key

Optional — without a key, REST requests are throttled to ~1 per 4 seconds.
A key unlocks higher rate limits for production use. Get one at [tonconsole.com](https://tonconsole.com/).

## Networks

| Network | Enum              | Base URL                    |
|---------|-------------------|-----------------------------|
| Mainnet | `Network.MAINNET` | `https://tonapi.io`         |
| Testnet | `Network.TESTNET` | `https://testnet.tonapi.io` |
| Tetra   | `Network.TETRA`   | `https://tetra.tonapi.io`   |

## Routing Table

| User intent                                    | Reference                      | Runner example                                      |
|------------------------------------------------|--------------------------------|-----------------------------------------------------|
| Installation, setup, first request             | `references/quickstart.md`     | —                                                   |
| SDK version                                    | —                              | `pytonapi -v`                                       |
| Account info, balance, jetton balances, events | `references/accounts.md`       | `accounts get_account --account-id EQ...`           |
| Blocks, transactions, validators, config       | `references/blockchain.md`     | `blockchain get_masterchain_head`                   |
| TonConnect payload, state init                 | `references/connect.md`        | `connect get_ton_connect_payload`                   |
| DNS domains, auctions, bids                    | `references/dns.md`            | `dns get_info --domain-name ton`                    |
| Message decoding, emulation                    | `references/emulation.md`      | `emulation decode_message --body {...}`             |
| Events by ID                                   | `references/events.md`         | `events get_event --event-id ...`                   |
| Extra currency info                            | `references/extra_currency.md` | `extra_currency get_info --id 1`                    |
| Gasless transfers                              | `references/gasless.md`        | `gasless config`                                    |
| Jetton info, holders, transfers                | `references/jettons.md`        | `jettons get_jetton_info --account-id EQ...`        |
| Raw liteserver operations                      | `references/lite_server.md`    | `lite_server get_raw_masterchain_info`              |
| Wallet migration, migratable assets            | `references/migration.md`      | `migration get_wallets --body {...}`                |
| Multisig wallets, orders                       | `references/multisig.md`       | `multisig get_account --account-id EQ...`           |
| NFT collections, items, history                | `references/nft.md`            | `nft get_collection --account-id EQ...`             |
| Purchase history                               | `references/purchases.md`      | `purchases get_purchase_history --account-id EQ...` |
| Token prices, charts, markets                  | `references/rates.md`          | `rates get_rates --tokens ton --currencies usd`     |
| Validators, validation rounds, rewards, APY    | `references/rewards.md`        | `rewards get_apy`                                   |
| Staking pools, nominators                      | `references/staking.md`        | `staking get_pools`                                 |
| TON storage providers                          | `references/storage.md`        | `storage get_providers`                             |
| Execution traces                               | `references/traces.md`         | `traces get_trace --trace-id ...`                   |
| API status, address parsing                    | `references/utilities.md`      | `utilities status`                                  |
| Wallet info, seqno, auth                       | `references/wallet.md`         | `wallet get_info --account-id EQ...`                |
| Real-time events (SSE/WebSocket)               | `references/streaming.md`      | `streaming sse --types transactions`                |
| Webhooks (push notifications)                  | `references/webhooks.md`       | — (generate code)                                   |

## Runner

Always run the runner from the **user's working directory**, not from the skill directory. Use `${CLAUDE_SKILL_DIR}` to
reference the script path:

```
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py <resource> <method> [--param value ...]
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py streaming <transport> [--types type ...]
```

Requires `pytonapi` package installed (`pip install pytonapi`).

Configuration priority: CLI flags > environment variables > defaults.

| Source  | API Key          | Network                             | Base URL          | RPS Limit          | RPS Period          |
|---------|------------------|-------------------------------------|-------------------|--------------------|---------------------|
| CLI     | `--api-key KEY`  | `--network mainnet\|testnet\|tetra` | `--base-url URL`  | `--rps-limit N`    | `--rps-period N`    |
| Env     | `TONAPI_API_KEY` | `TONAPI_NETWORK`                    | `TONAPI_BASE_URL` | `TONAPI_RPS_LIMIT` | `TONAPI_RPS_PERIOD` |
| Default | — (optional)     | `mainnet`                           | auto by network   | `0` (disabled)     | `1.0`               |

## Key Rotation

REST — pass `ApiKey` objects with per-key rate limits:

```python
from pytonapi.types import ApiKey

TonapiRestClient(api_key=[ApiKey("key-1", rps_limit=5), ApiKey("key-2", rps_limit=10)])
```

On 429 (after all retries for current key), rotates to the next key with its own rate limiter.

Same-plan keys share combined server-side RPS; different-plan keys have independent limits.

## When to Execute vs Generate Code

**Execute via runner** — user wants concrete data ("balance of X", "show NFT Y"), single API call, no complex logic.

**Generate SDK code** — user is building an app, streaming/webhook scenarios, multiple calls with conditions, or
explicitly asks for code.

## Retries

SDK retries `429` (5 attempts, 0.3s base) and `500, 502, 503, 504` (3 attempts, 0.5s base) with exponential backoff.
Retries configurable via `RetryPolicy` or disabled with `retry_policy=None`.

## Error Handling

- No API key → SDK auto-limits to ~1 request per 4 seconds; inform user a key from [tonconsole.com](https://tonconsole.com/) unlocks higher limits
- 401 → invalid API key, direct user to [tonconsole.com](https://tonconsole.com/)
- 403 → check API key permissions
- 404 → explain meaning (address not found, transaction not found, etc.)
- 429 → SDK retries automatically with key rotation if multiple keys provided; if persistent, suggest upgrading plan
- `TONAPIValidationError` → response body didn't match Pydantic model; likely API change, report to developer
- Never guess addresses or parameters — ask the user

## Signing and Sending Transactions

The SDK can send a signed BOC (`blockchain.send_message`), but cannot sign transactions — it has no access to
private keys.
For building and signing transactions, recommend `tonutils` (`pip install tonutils`).

## Addresses

- Accept any format (raw, bounceable, non-bounceable) — TONAPI handles all
- Don't convert addresses without explicit request

## Import Paths

```python
from pytonapi.rest import TonapiRestClient
from pytonapi.types import Network, Workchain, Opcode, ApiKey, RetryPolicy, RetryRule, ReconnectPolicy, DEFAULT_RETRY_POLICY, DEFAULT_RECONNECT_POLICY
from pytonapi.streaming import TonapiSSE, TonapiWebSocket
from pytonapi.streaming import Finality, ConnectionState, EventType, ActionType
from pytonapi.streaming import TransactionsNotification, ActionsNotification, TraceNotification
from pytonapi.streaming import AccountStateNotification, JettonsNotification, TraceInvalidatedNotification
from pytonapi.streaming import AccountState, JettonWallet, StreamNotification
from pytonapi.webhook import TonapiWebhookClient, TonapiWebhookDispatcher, TonapiWebhook
from pytonapi.webhook import WebhookEventType, AccountTxEvent, MempoolMsgEvent, OpcodeMsgEvent, NewContractsEvent
from pytonapi.utils import raw_to_userfriendly, userfriendly_to_raw, to_nano, to_amount
from pytonapi.exceptions import TONAPIError, TONAPIClientError, TONAPINotFoundError, TONAPIValidationError
```

Never use `from pytonapi import ...` — the root package has no re-exports.

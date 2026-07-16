# 📦 TON API

[![TON](https://img.shields.io/badge/TON-grey?logo=TON&logoColor=40AEF0)](https://ton.org)
![Python Versions](https://img.shields.io/badge/Python-3.10%20--%203.14-black?color=FFE873&labelColor=3776AB)
[![PyPI](https://img.shields.io/pypi/v/pytonapi.svg?color=FFE873&labelColor=3776AB)](https://pypi.python.org/pypi/pytonapi)
[![License](https://img.shields.io/github/license/nessshon/tonapi)](https://github.com/nessshon/tonapi/blob/main/LICENSE)
[![Donate](https://img.shields.io/badge/Donate-TON-blue)](https://tonviewer.com/UQCZq3_Vd21-4y4m7Wc-ej9NFOhh_qvdfAkAYAOHoQ__Ness)

![Image](https://raw.githubusercontent.com/nessshon/tonapi/main/banner.png)

![Downloads](https://pepy.tech/badge/pytonapi)
![Downloads](https://pepy.tech/badge/pytonapi/month)
![Downloads](https://pepy.tech/badge/pytonapi/week)
[![Context7](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcontext7.com%2Fapi%2Fv2%2Flibs%2Fsearch%3FlibraryName%3Dnessshon%2Ftonapi%26query%3Dtonapi&query=%24.results%5B0%5D.benchmarkScore&label=Context7&suffix=%2F100&color=blue)](https://context7.com/nessshon/tonapi)

### Python SDK for [TON API](https://tonapi.io)

Access TON blockchain data via REST API, real-time streaming, and webhooks.  
API key optional for REST, required for streaming and webhooks — obtain at [tonconsole.com](https://tonconsole.com/).

> For creating wallets, transferring TON, jettons, etc., use [tonutils](https://github.com/nessshon/tonutils).

**Features**

- **REST API** — accounts, NFTs, jettons, DNS, and more
- **Streaming** — real-time events via SSE and WebSocket
- **Webhooks** — push notifications with event dispatcher

> Support this project — TON: `donate.ness.ton`  
> `UQCZq3_Vd21-4y4m7Wc-ej9NFOhh_qvdfAkAYAOHoQ__Ness`

## Installation

```bash
pip install pytonapi
```

[Claude Code plugin](https://github.com/nessshon/tonapi/blob/main/skills/tonapi/README.md):
```
/plugin marketplace add nessshon/claude-plugins
/plugin install tonapi@nessshon-plugins
```

## Documentation

[Documentation](https://tonapi.ness.uz/) — API reference, streaming, and webhooks guides.  
[llms.txt](https://tonapi.ness.uz/llms.txt) — auto-generated machine-readable docs for AI tools.

## Examples

**REST API**

- [Get account info](https://github.com/nessshon/tonapi/blob/main/examples/get_account_info.py)
- [Get account transactions](https://github.com/nessshon/tonapi/blob/main/examples/get_account_transactions.py)
- [Get jetton info](https://github.com/nessshon/tonapi/blob/main/examples/get_jetton_info.py)
- [Get NFTs by owner](https://github.com/nessshon/tonapi/blob/main/examples/get_nft_by_owner.py)
- [Get NFTs by collection](https://github.com/nessshon/tonapi/blob/main/examples/get_nft_by_collection.py)

**Emulation & Sending**

- [Send message](https://github.com/nessshon/tonapi/blob/main/examples/send_message.py)
- [Emulate message](https://github.com/nessshon/tonapi/blob/main/examples/emulate_message.py)

**Transfers** (requires [tonutils](https://github.com/nessshon/tonutils))

- [Transfer TON](https://github.com/nessshon/tonapi/blob/main/examples/transfer_ton.py)
- [Gasless transfer](https://github.com/nessshon/tonapi/blob/main/examples/transfer_gasless.py)

**Streaming** (SSE & WebSocket)

- [SSE subscriptions](https://github.com/nessshon/tonapi/blob/main/examples/streaming_sse.py)
- [WebSocket subscriptions](https://github.com/nessshon/tonapi/blob/main/examples/streaming_websocket.py)

**Webhooks**

- [FastAPI webhook server](https://github.com/nessshon/tonapi/blob/main/examples/webhook_fastapi.py)
- [aiohttp webhook server](https://github.com/nessshon/tonapi/blob/main/examples/webhook_aiohttp.py)

## License

This repository is distributed under the [MIT License](https://github.com/nessshon/tonapi/blob/main/LICENSE).

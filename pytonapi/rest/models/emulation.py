# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, Field

if t.TYPE_CHECKING:
    from pytonapi.rest.models.accounts import AccountAddress, AccountEvent, JettonPreview
    from pytonapi.rest.models.nft import NftItem
    from pytonapi.rest.models.traces import Trace


class DecodedMessage(BaseModel):
    destination: AccountAddress
    destination_wallet_version: str
    ext_in_msg_decoded: t.Any | None = Field(default=None)


class DecodedRawMessage(BaseModel):
    message: t.Any
    mode: int


class JettonQuantity(BaseModel):
    quantity: str
    wallet_address: AccountAddress
    jetton: JettonPreview


class Risk(BaseModel):
    transfer_all_remaining_balance: bool
    gram: int
    jettons: list[JettonQuantity]
    nfts: list[NftItem]
    ton: int | None = Field(default=None)
    total_equivalent: float | None = Field(default=None)


class MessageConsequences(BaseModel):
    trace: Trace
    risk: Risk
    event: AccountEvent

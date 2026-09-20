# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, ConfigDict, Field

from pytonapi.rest.models._enums import AccountStatus

if t.TYPE_CHECKING:
    from pytonapi.rest.models.accounts import JettonBalance
    from pytonapi.rest.models.emulation import MessageConsequences


class InsufficientFunds(BaseModel):
    required: int
    available: int


class MigrationOutMessage(BaseModel):
    boc: str
    mode: int


class MigrationPrepareConflict(BaseModel):
    pass


class MigrationPrepareRequest(BaseModel):
    from_: str = Field(alias="from")
    to: str
    currency: str | None = Field(default=None)
    public_key: str | None = Field(default=None)
    gas_payer: str | None = Field(default=None)
    gas_jetton_master: str | None = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)


class MigrationTransaction(BaseModel):
    seqno: int
    boc: str
    messages: list[MigrationOutMessage]
    emulation: MessageConsequences
    gas_spent: int
    sponsored: bool | None = Field(default=None)
    commission: str | None = Field(default=None)
    state_init: str | None = Field(default=None)


class MigrationPrepareResponse(BaseModel):
    from_: str = Field(alias="from")
    to: str
    wallet_version: str
    transactions: list[MigrationTransaction]

    model_config = ConfigDict(populate_by_name=True)


class MigrationWalletValue(BaseModel):
    account: str
    balance: int
    status: AccountStatus
    jettons: list[JettonBalance]
    nft_count: int


class MigrationWallets(BaseModel):
    wallets: list[MigrationWalletValue]

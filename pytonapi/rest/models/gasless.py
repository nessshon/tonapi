# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, ConfigDict, Field

if t.TYPE_CHECKING:
    from pytonapi.rest.models.emulation import MessageConsequences


class GaslessConfig(BaseModel):
    relay_address: str
    gas_jettons: list[t.Any]


class GaslessTx(BaseModel):
    protocol_name: str
    external: str | None = Field(default=None)


class SignRawMessage(BaseModel):
    address: str
    amount: str
    payload: str | None = Field(default=None)
    state_init: str | None = Field(alias="stateInit", default=None)

    model_config = ConfigDict(populate_by_name=True)


class SignRawParams(BaseModel):
    protocol_name: str
    relay_address: str
    commission: str
    from_: str = Field(alias="from")
    valid_until: int
    messages: list[SignRawMessage]
    emulation: MessageConsequences | None = Field(default=None)

    model_config = ConfigDict(populate_by_name=True)

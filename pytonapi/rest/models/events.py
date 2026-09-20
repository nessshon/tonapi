# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, Field

if t.TYPE_CHECKING:
    from pytonapi.rest.models.accounts import AccountAddress, Action


class ValueFlow(BaseModel):
    account: AccountAddress
    gram: int
    fees: int
    ton: int | None = Field(default=None)
    jettons: list[t.Any] | None = Field(default=None)


class Event(BaseModel):
    event_id: str
    timestamp: int
    actions: list[Action]
    value_flow: list[ValueFlow]
    is_scam: bool
    lt: int
    in_progress: bool
    progress: float
    last_slice_id: int | None = Field(default=None)
    ext_msg_hash: str | None = Field(default=None)

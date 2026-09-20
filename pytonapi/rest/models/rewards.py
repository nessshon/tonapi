# This file is auto-generated. Do not edit manually.

from __future__ import annotations

from pydantic import BaseModel, Field


class BlockInfo(BaseModel):
    seqno: int
    utime: int | None = Field(default=None)


class NominatorRewardEntry(BaseModel):
    address: str
    weight: float
    reward: int
    effective_stake: int
    stake: int


class RewardsStats(BaseModel):
    apy: list[list[float]]
    total_stake: list[list[float]]


class RoundInfo(BaseModel):
    start_block: int
    end_block: int
    start_utime: int | None = Field(default=None)
    end_utime: int | None = Field(default=None)


class ValidatorRewardEntry(BaseModel):
    rank: int
    public_key: str
    effective_stake: int
    weight: float
    reward: int
    pool: str | None = Field(default=None)
    pool_type: str | None = Field(default=None)
    owner_address: str | None = Field(default=None)
    validator_address: str | None = Field(default=None)
    validator_stake: int | None = Field(default=None)
    nominators_stake: int | None = Field(default=None)
    total_stake: int | None = Field(default=None)
    validator_reward_share: float | None = Field(default=None)
    nominators_count: int | None = Field(default=None)
    nominators: list[NominatorRewardEntry] | None = Field(default=None)


class RoundRewardsResponse(BaseModel):
    response_time_ms: int
    election_id: int
    round_start: str
    round_end: str
    start_block: int
    end_block: int
    total_bonuses: int
    total_stake: int
    validators: list[ValidatorRewardEntry]
    prev_election_id: int | None = Field(default=None)
    next_election_id: int | None = Field(default=None)
    error: str | None = Field(default=None)


class ValidationRound(BaseModel):
    election_id: int
    start_block: int
    finished: bool
    start_utime: int | None = Field(default=None)
    end_utime: int | None = Field(default=None)
    end_block: int | None = Field(default=None)
    prev_election_id: int | None = Field(default=None)
    next_election_id: int | None = Field(default=None)
    total_stake: int | None = Field(default=None)
    bonuses: int | None = Field(default=None)


class ValidationRoundsResponse(BaseModel):
    response_time_ms: int
    rounds: list[ValidationRound]


class ValidatorsResponse(BaseModel):
    response_time_ms: int
    block: BlockInfo
    validation_round: RoundInfo
    election_id: int
    elector_balance: int
    total_stake: int
    reward_per_block: int
    validators: list[ValidatorRewardEntry]
    prev_election_id: int | None = Field(default=None)
    next_election_id: int | None = Field(default=None)

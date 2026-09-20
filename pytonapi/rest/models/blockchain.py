# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, ConfigDict, Field

from pytonapi.rest.models._enums import (
    AccountStatus,
    AccStatusChange,
    BouncePhaseType,
    ComputeSkipReason,
    TransactionType,
)

if t.TYPE_CHECKING:
    from pytonapi.rest.models.accounts import AccountAddress, ExtraCurrency


class AccountStorageInfo(BaseModel):
    used_cells: int
    used_bits: int
    used_public_cells: int
    last_paid: int
    due_payment: int


class ActionPhase(BaseModel):
    success: bool
    result_code: int
    total_actions: int
    skipped_actions: int
    fwd_fees: int
    total_fees: int
    result_code_description: str | None = Field(default=None)


class BlockCurrencyCollection(BaseModel):
    grams: int
    other: list[t.Any]


class BlockParamLimits(BaseModel):
    underload: int
    soft_limit: int
    hard_limit: int


class BlockLimits(BaseModel):
    bytes: BlockParamLimits
    gas: BlockParamLimits
    lt_delta: BlockParamLimits


class BlockValueFlow(BaseModel):
    from_prev_blk: BlockCurrencyCollection
    to_next_blk: BlockCurrencyCollection
    imported: BlockCurrencyCollection
    exported: BlockCurrencyCollection
    fees_collected: BlockCurrencyCollection
    fees_imported: BlockCurrencyCollection
    recovered: BlockCurrencyCollection
    created: BlockCurrencyCollection
    minted: BlockCurrencyCollection
    burned: BlockCurrencyCollection | None = Field(default=None)


class Method(BaseModel):
    id: int
    method: str


class SourceFile(BaseModel):
    name: str
    content: str
    is_entrypoint: bool
    is_std_lib: bool
    include_in_command: bool


class Source(BaseModel):
    files: list[SourceFile]


class BlockchainAccountInspect(BaseModel):
    code: str
    code_hash: str
    methods: list[Method]
    compiler: str
    disassembled_code: str | None = Field(default=None)
    source: Source | None = Field(default=None)


class BlockchainBlock(BaseModel):
    tx_quantity: int
    value_flow: BlockValueFlow
    workchain_id: int
    shard: str
    seqno: int
    root_hash: str
    file_hash: str
    global_id: int
    version: int
    after_merge: bool
    before_split: bool
    after_split: bool
    want_split: bool
    want_merge: bool
    key_block: bool
    gen_utime: int
    start_lt: int
    end_lt: int
    vert_seqno: int
    gen_catchain_seqno: int
    min_ref_mc_seqno: int
    prev_key_block_seqno: int
    prev_refs: list[str]
    in_msg_descr_length: int
    out_msg_descr_length: int
    rand_seed: str
    created_by: str
    gen_software_version: int | None = Field(default=None)
    gen_software_capabilities: int | None = Field(default=None)
    master_ref: str | None = Field(default=None)


class BlockchainBlockShards(BaseModel):
    shards: list[t.Any]


class BlockchainBlocks(BaseModel):
    blocks: list[BlockchainBlock]


class ValidatorsSet(BaseModel):
    utime_since: int
    utime_until: int
    total: int
    main: int
    list: list[t.Any]
    total_weight: str | None = Field(default=None)


class BlockchainConfig(BaseModel):
    raw: str
    p0: str = Field(alias="0")
    p1: str = Field(alias="1")
    p2: str = Field(alias="2")
    p4: str = Field(alias="4")
    p44: t.Any = Field(alias="44")
    p3: str | None = Field(alias="3", default=None)
    p5: t.Any | None = Field(alias="5", default=None)
    p6: t.Any | None = Field(alias="6", default=None)
    p7: t.Any | None = Field(alias="7", default=None)
    p8: t.Any | None = Field(alias="8", default=None)
    p9: t.Any | None = Field(alias="9", default=None)
    p10: t.Any | None = Field(alias="10", default=None)
    p11: t.Any | None = Field(alias="11", default=None)
    p12: t.Any | None = Field(alias="12", default=None)
    p13: t.Any | None = Field(alias="13", default=None)
    p14: t.Any | None = Field(alias="14", default=None)
    p15: t.Any | None = Field(alias="15", default=None)
    p16: t.Any | None = Field(alias="16", default=None)
    p17: t.Any | None = Field(alias="17", default=None)
    p18: t.Any | None = Field(alias="18", default=None)
    p20: t.Any | None = Field(alias="20", default=None)
    p21: t.Any | None = Field(alias="21", default=None)
    p22: t.Any | None = Field(alias="22", default=None)
    p23: t.Any | None = Field(alias="23", default=None)
    p24: t.Any | None = Field(alias="24", default=None)
    p25: t.Any | None = Field(alias="25", default=None)
    p28: t.Any | None = Field(alias="28", default=None)
    p29: t.Any | None = Field(alias="29", default=None)
    p30: t.Any | None = Field(alias="30", default=None)
    p31: t.Any | None = Field(alias="31", default=None)
    p32: ValidatorsSet | None = Field(alias="32", default=None)
    p33: ValidatorsSet | None = Field(alias="33", default=None)
    p34: ValidatorsSet | None = Field(alias="34", default=None)
    p35: ValidatorsSet | None = Field(alias="35", default=None)
    p36: ValidatorsSet | None = Field(alias="36", default=None)
    p37: ValidatorsSet | None = Field(alias="37", default=None)
    p40: t.Any | None = Field(alias="40", default=None)
    p43: t.Any | None = Field(alias="43", default=None)
    p45: t.Any | None = Field(alias="45", default=None)
    p71: t.Any | None = Field(alias="71", default=None)
    p72: t.Any | None = Field(alias="72", default=None)
    p73: t.Any | None = Field(alias="73", default=None)
    p79: t.Any | None = Field(alias="79", default=None)
    p81: t.Any | None = Field(alias="81", default=None)
    p82: t.Any | None = Field(alias="82", default=None)

    model_config = ConfigDict(populate_by_name=True)


class BlockchainLibrary(BaseModel):
    boc: str


class BlockchainRawAccount(BaseModel):
    address: str
    balance: int
    last_transaction_lt: int
    status: AccountStatus
    storage: AccountStorageInfo
    extra_balance: list[ExtraCurrency] | None = Field(default=None)
    code: str | None = Field(default=None)
    data: str | None = Field(default=None)
    last_transaction_hash: str | None = Field(default=None)
    frozen_hash: str | None = Field(default=None)
    libraries: list[t.Any] | None = Field(default=None)


class BlockchainRawAccounts(BaseModel):
    accounts: list[BlockchainRawAccount]


class ComputePhase(BaseModel):
    skipped: bool
    skip_reason: ComputeSkipReason | None = Field(default=None)
    success: bool | None = Field(default=None)
    gas_fees: int | None = Field(default=None)
    gas_used: int | None = Field(default=None)
    vm_steps: int | None = Field(default=None)
    exit_code: int | None = Field(default=None)
    exit_code_description: str | None = Field(default=None)


class ConfigProposalSetup(BaseModel):
    min_tot_rounds: int
    max_tot_rounds: int
    min_wins: int
    max_losses: int
    min_store_sec: int
    max_store_sec: int
    bit_price: int
    cell_price: int


class CreditPhase(BaseModel):
    fees_collected: int
    credit: int


class Error(BaseModel):
    error: str


class GasLimitPrices(BaseModel):
    gas_price: int
    gas_limit: int
    gas_credit: int
    block_gas_limit: int
    freeze_due_limit: int
    delete_due_limit: int
    special_gas_limit: int | None = Field(default=None)
    flat_gas_limit: int | None = Field(default=None)
    flat_gas_price: int | None = Field(default=None)


class JettonBridgePrices(BaseModel):
    bridge_burn_fee: int
    bridge_mint_fee: int
    wallet_min_gram_for_storage: int
    wallet_gas_consumption: int
    minter_min_gram_for_storage: int
    discover_gas_consumption: int
    wallet_min_tons_for_storage: int | None = Field(default=None)
    minter_min_tons_for_storage: int | None = Field(default=None)


class Oracle(BaseModel):
    address: str
    secp_pubkey: str


class JettonBridgeParams(BaseModel):
    bridge_address: str
    oracles_address: str
    state_flags: int
    oracles: list[Oracle]
    burn_bridge_fee: int | None = Field(default=None)
    external_chain_address: str | None = Field(default=None)
    prices: JettonBridgePrices | None = Field(default=None)


class StateInit(BaseModel):
    boc: str
    interfaces: list[str]


class Message(BaseModel):
    msg_type: str
    created_lt: int
    ihr_disabled: bool
    bounce: bool
    bounced: bool
    value: int
    fwd_fee: int
    ihr_fee: int
    import_fee: int
    created_at: int
    hash: str
    value_extra: list[ExtraCurrency] | None = Field(default=None)
    destination: AccountAddress | None = Field(default=None)
    source: AccountAddress | None = Field(default=None)
    op_code: str | None = Field(default=None)
    init: StateInit | None = Field(default=None)
    raw_body: str | None = Field(default=None)
    decoded_op_name: str | None = Field(default=None)
    decoded_body: t.Any | None = Field(default=None)


class TvmStackRecord(BaseModel):
    type: str
    cell: str | None = Field(default=None)
    slice: str | None = Field(default=None)
    num: str | None = Field(default=None)
    tuple: list[TvmStackRecord] | None = Field(default=None)


class MethodExecutionResult(BaseModel):
    success: bool
    exit_code: int
    stack: list[TvmStackRecord]
    decoded: t.Any | None = Field(default=None)


class MisbehaviourPunishmentConfig(BaseModel):
    default_flat_fine: int
    default_proportional_fine: int
    severity_flat_mult: int
    severity_proportional_mult: int
    unpunishable_interval: int
    long_interval: int
    long_flat_mult: int
    long_proportional_mult: int
    medium_interval: int
    medium_flat_mult: int
    medium_proportional_mult: int


class MsgForwardPrices(BaseModel):
    lump_price: int
    bit_price: int
    cell_price: int
    ihr_price_factor: int
    first_frac: int
    next_frac: int


class NewConsensusConfig(BaseModel):
    flags: int
    use_quic: bool
    slots_per_leader_window: int
    target_rate_ms: int | None = Field(default=None)
    first_block_timeout_ms: int | None = Field(default=None)
    max_leader_window_desync: int | None = Field(default=None)
    noncritical_params: dict[str, int] | None = Field(default=None)


class OracleBridgeParams(BaseModel):
    bridge_addr: str
    oracle_multisig_address: str
    external_chain_address: str
    oracles: list[Oracle]


class RawBlockchainConfig(BaseModel):
    config: dict[str, t.Any]


class ReducedBlock(BaseModel):
    workchain_id: int
    shard: str
    seqno: int
    tx_quantity: int
    utime: int
    shards_blocks: list[str]
    parent: list[str]
    master_ref: str | None = Field(default=None)


class ReducedBlocks(BaseModel):
    blocks: list[ReducedBlock]


class SizeLimitsConfig(BaseModel):
    max_msg_bits: int
    max_msg_cells: int
    max_library_cells: int
    max_vm_data_depth: int
    max_ext_msg_size: int
    max_ext_msg_depth: int
    max_acc_state_cells: int | None = Field(default=None)
    max_acc_state_bits: int | None = Field(default=None)


class StoragePhase(BaseModel):
    fees_collected: int
    status_change: AccStatusChange
    fees_due: int | None = Field(default=None)


class Transaction(BaseModel):
    hash: str
    lt: int
    account: AccountAddress
    success: bool
    utime: int
    orig_status: AccountStatus
    end_status: AccountStatus
    total_fees: int
    end_balance: int
    transaction_type: TransactionType
    state_update_old: str
    state_update_new: str
    out_msgs: list[Message]
    block: str
    aborted: bool
    destroyed: bool
    raw: str
    in_msg: Message | None = Field(default=None)
    prev_trans_hash: str | None = Field(default=None)
    prev_trans_lt: int | None = Field(default=None)
    compute_phase: ComputePhase | None = Field(default=None)
    storage_phase: StoragePhase | None = Field(default=None)
    credit_phase: CreditPhase | None = Field(default=None)
    action_phase: ActionPhase | None = Field(default=None)
    bounce_phase: BouncePhaseType | None = Field(default=None)


class Transactions(BaseModel):
    transactions: list[Transaction]


class Validator(BaseModel):
    address: str
    adnl_address: str
    stake: int
    max_factor: int


class Validators(BaseModel):
    elect_at: int
    elect_close: int
    min_stake: int
    total_stake: int
    validators: list[Validator]


class WorkchainDescr(BaseModel):
    workchain: int
    enabled_since: int
    actual_min_split: int
    min_split: int
    max_split: int
    basic: int
    active: bool
    accept_msgs: bool
    flags: int
    zerostate_root_hash: str
    zerostate_file_hash: str
    version: int

# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, ConfigDict, Field

from pytonapi.rest.models._enums import (
    AccountStatus,
    CurrencyType,
    DefiAssetType,
    ExecGetMethodArgType,
    JettonVerificationType,
    PoolImplementationType,
    TrustType,
)

if t.TYPE_CHECKING:
    from pytonapi.rest.models.extra_currency import EcPreview
    from pytonapi.rest.models.jettons import ScaledUI
    from pytonapi.rest.models.multisig import Multisig
    from pytonapi.rest.models.nft import NftItem
    from pytonapi.rest.models.rates import TokenRates


class ExtraCurrency(BaseModel):
    amount: str
    preview: EcPreview


class Account(BaseModel):
    address: str
    balance: int
    last_activity: int
    status: AccountStatus
    get_methods: list[str]
    is_wallet: bool
    extra_balance: list[ExtraCurrency] | None = Field(default=None)
    currencies_balance: dict[str, t.Any] | None = Field(default=None)
    interfaces: list[str] | None = Field(default=None)
    name: str | None = Field(default=None)
    is_scam: bool | None = Field(default=None)
    icon: str | None = Field(default=None)
    memo_required: bool | None = Field(default=None)
    is_suspended: bool | None = Field(default=None)


class AccountAddress(BaseModel):
    address: str
    is_scam: bool
    is_wallet: bool
    name: str | None = Field(default=None)
    icon: str | None = Field(default=None)


class ActionSimplePreview(BaseModel):
    name: str
    description: str
    accounts: list[AccountAddress]
    action_image: str | None = Field(default=None)
    value: str | None = Field(default=None)
    fiat_value: str | None = Field(default=None)
    value_image: str | None = Field(default=None)


class AddExtensionAction(BaseModel):
    wallet: AccountAddress
    extension: str


class Price(BaseModel):
    currency_type: CurrencyType
    value: str
    decimals: int
    token_name: str
    verification: TrustType
    image: str
    jetton: str | None = Field(default=None)


class AuctionBidAction(BaseModel):
    auction_type: str
    amount: Price
    bidder: AccountAddress
    auction: AccountAddress
    nft: NftItem | None = Field(default=None)


class BuyXTRAction(BaseModel):
    recipient: AccountAddress
    amount: str


class ContractDeployAction(BaseModel):
    address: str
    interfaces: list[str]


class DepositStakeAction(BaseModel):
    amount: int
    staker: AccountAddress
    pool: AccountAddress
    implementation: PoolImplementationType
    stake_meta: Price | None = Field(default=None)


class Protocol(BaseModel):
    name: str
    image: str | None = Field(default=None)


class DepositTokenStakeAction(BaseModel):
    staker: AccountAddress
    protocol: Protocol
    stake_meta: Price | None = Field(default=None)


class DepositXTRAction(BaseModel):
    recipient: AccountAddress
    amount: str


class DomainRenewAction(BaseModel):
    domain: str
    contract_address: str
    renewer: AccountAddress


class ElectionsDepositStakeAction(BaseModel):
    amount: int
    staker: AccountAddress


class ElectionsRecoverStakeAction(BaseModel):
    amount: int
    staker: AccountAddress


class EncryptedComment(BaseModel):
    encryption_type: str
    cipher_text: str


class ExtraCurrencyTransferAction(BaseModel):
    sender: AccountAddress
    recipient: AccountAddress
    amount: str
    currency: EcPreview
    comment: str | None = Field(default=None)
    encrypted_comment: EncryptedComment | None = Field(default=None)


class JettonPreview(BaseModel):
    address: str
    name: str
    symbol: str
    decimals: int
    image: str
    verification: JettonVerificationType
    score: int
    custom_payload_api_uri: str | None = Field(default=None)
    scaled_ui: ScaledUI | None = Field(default=None)
    description: str | None = Field(default=None)


class Refund(BaseModel):
    type: str
    origin: str


class FlawedJettonTransferAction(BaseModel):
    senders_wallet: str
    recipients_wallet: str
    sent_amount: str
    received_amount: str
    jetton: JettonPreview
    sender: AccountAddress | None = Field(default=None)
    recipient: AccountAddress | None = Field(default=None)
    comment: str | None = Field(default=None)
    encrypted_comment: EncryptedComment | None = Field(default=None)
    refund: Refund | None = Field(default=None)


class GasRelayFee(BaseModel):
    jetton: JettonPreview
    amount: str


class GasRelayAction(BaseModel):
    amount: int
    relayer: AccountAddress
    target: AccountAddress
    is_battery: bool | None = Field(default=None)
    relayer_fee: GasRelayFee | None = Field(default=None)


class JettonBurnAction(BaseModel):
    sender: AccountAddress
    senders_wallet: str
    amount: str
    jetton: JettonPreview


class JettonMintAction(BaseModel):
    recipient: AccountAddress
    recipients_wallet: str
    amount: str
    jetton: JettonPreview


class JettonSwapAction(BaseModel):
    dex: str
    amount_in: str
    amount_out: str
    user_wallet: AccountAddress
    router: AccountAddress
    ton_in: int | None = Field(default=None)
    ton_out: int | None = Field(default=None)
    gram_in: int | None = Field(default=None)
    gram_out: int | None = Field(default=None)
    jetton_master_in: JettonPreview | None = Field(default=None)
    jetton_master_out: JettonPreview | None = Field(default=None)


class JettonTransferAction(BaseModel):
    senders_wallet: str
    recipients_wallet: str
    amount: str
    jetton: JettonPreview
    sender: AccountAddress | None = Field(default=None)
    recipient: AccountAddress | None = Field(default=None)
    comment: str | None = Field(default=None)
    encrypted_comment: EncryptedComment | None = Field(default=None)
    refund: Refund | None = Field(default=None)


class VaultDepositInfo(BaseModel):
    price: Price
    vault: str


class LiquidityDepositAction(BaseModel):
    protocol: Protocol
    from_: AccountAddress = Field(alias="from")
    tokens: list[VaultDepositInfo]

    model_config = ConfigDict(populate_by_name=True)


class NftItemTransferAction(BaseModel):
    nft: str
    sender: AccountAddress | None = Field(default=None)
    recipient: AccountAddress | None = Field(default=None)
    comment: str | None = Field(default=None)
    encrypted_comment: EncryptedComment | None = Field(default=None)
    payload: str | None = Field(default=None)
    refund: Refund | None = Field(default=None)


class NftPurchaseAction(BaseModel):
    auction_type: str
    amount: Price
    nft: NftItem
    seller: AccountAddress
    buyer: AccountAddress


class OraclePriceFeed(BaseModel):
    id: str
    display_symbol: str
    rate: float | None = Field(default=None)


class OracleRequestAction(BaseModel):
    requester: AccountAddress
    response_to: AccountAddress
    price_feeds: list[OraclePriceFeed]


class Metadata(BaseModel):
    encrypted_binary: str
    decryption_key: str | None = Field(default=None)


class PurchaseAction(BaseModel):
    source: AccountAddress
    destination: AccountAddress
    invoice_id: str
    amount: Price
    metadata: Metadata


class RemoveExtensionAction(BaseModel):
    wallet: AccountAddress
    extension: str


class SetSignatureAllowedAction(BaseModel):
    wallet: AccountAddress
    allowed: bool


class SmartContractAction(BaseModel):
    executor: AccountAddress
    contract: AccountAddress
    gram_attached: int
    operation: str
    ton_attached: int | None = Field(default=None)
    payload: str | None = Field(default=None)
    refund: Refund | None = Field(default=None)


class SubscriptionAction(BaseModel):
    subscriber: AccountAddress
    subscription: str
    beneficiary: AccountAddress
    admin: AccountAddress
    price: Price
    initial: bool
    amount: int | None = Field(default=None)


class TonTransferAction(BaseModel):
    sender: AccountAddress
    recipient: AccountAddress
    amount: int
    comment: str | None = Field(default=None)
    encrypted_comment: EncryptedComment | None = Field(default=None)
    refund: Refund | None = Field(default=None)


class UnSubscriptionAction(BaseModel):
    subscriber: AccountAddress
    subscription: str
    beneficiary: AccountAddress
    admin: AccountAddress


class WithdrawStakeAction(BaseModel):
    amount: int
    staker: AccountAddress
    pool: AccountAddress
    implementation: PoolImplementationType


class WithdrawStakeRequestAction(BaseModel):
    staker: AccountAddress
    pool: AccountAddress
    implementation: PoolImplementationType
    amount: int | None = Field(default=None)
    stake_meta: Price | None = Field(default=None)


class WithdrawTokenStakeRequestAction(BaseModel):
    staker: AccountAddress
    protocol: Protocol
    stake_meta: Price | None = Field(default=None)


class WithdrawXTRAction(BaseModel):
    user: AccountAddress
    amount: str


class Action(BaseModel):
    type: str
    status: str
    simple_preview: ActionSimplePreview
    base_transactions: list[str]
    ton_transfer: TonTransferAction | None = Field(alias="TonTransfer", default=None)
    extra_currency_transfer: ExtraCurrencyTransferAction | None = Field(alias="ExtraCurrencyTransfer", default=None)
    contract_deploy: ContractDeployAction | None = Field(alias="ContractDeploy", default=None)
    jetton_transfer: JettonTransferAction | None = Field(alias="JettonTransfer", default=None)
    flawed_jetton_transfer: FlawedJettonTransferAction | None = Field(alias="FlawedJettonTransfer", default=None)
    jetton_burn: JettonBurnAction | None = Field(alias="JettonBurn", default=None)
    jetton_mint: JettonMintAction | None = Field(alias="JettonMint", default=None)
    nft_item_transfer: NftItemTransferAction | None = Field(alias="NftItemTransfer", default=None)
    subscribe: SubscriptionAction | None = Field(alias="Subscribe", default=None)
    un_subscribe: UnSubscriptionAction | None = Field(alias="UnSubscribe", default=None)
    auction_bid: AuctionBidAction | None = Field(alias="AuctionBid", default=None)
    nft_purchase: NftPurchaseAction | None = Field(alias="NftPurchase", default=None)
    deposit_stake: DepositStakeAction | None = Field(alias="DepositStake", default=None)
    withdraw_stake: WithdrawStakeAction | None = Field(alias="WithdrawStake", default=None)
    withdraw_stake_request: WithdrawStakeRequestAction | None = Field(alias="WithdrawStakeRequest", default=None)
    elections_deposit_stake: ElectionsDepositStakeAction | None = Field(alias="ElectionsDepositStake", default=None)
    elections_recover_stake: ElectionsRecoverStakeAction | None = Field(alias="ElectionsRecoverStake", default=None)
    jetton_swap: JettonSwapAction | None = Field(alias="JettonSwap", default=None)
    smart_contract_exec: SmartContractAction | None = Field(alias="SmartContractExec", default=None)
    domain_renew: DomainRenewAction | None = Field(alias="DomainRenew", default=None)
    purchase: PurchaseAction | None = Field(alias="Purchase", default=None)
    add_extension: AddExtensionAction | None = Field(alias="AddExtension", default=None)
    remove_extension: RemoveExtensionAction | None = Field(alias="RemoveExtension", default=None)
    set_signature_allowed_action: SetSignatureAllowedAction | None = Field(
        alias="SetSignatureAllowedAction", default=None
    )
    gas_relay: GasRelayAction | None = Field(alias="GasRelay", default=None)
    deposit_token_stake: DepositTokenStakeAction | None = Field(alias="DepositTokenStake", default=None)
    withdraw_token_stake_request: WithdrawTokenStakeRequestAction | None = Field(
        alias="WithdrawTokenStakeRequest", default=None
    )
    liquidity_deposit: LiquidityDepositAction | None = Field(alias="LiquidityDeposit", default=None)
    oracle_request: OracleRequestAction | None = Field(alias="OracleRequest", default=None)
    withdraw_xtr: WithdrawXTRAction | None = Field(alias="WithdrawXTR", default=None)
    deposit_xtr: DepositXTRAction | None = Field(alias="DepositXTR", default=None)
    buy_xtr: BuyXTRAction | None = Field(alias="BuyXTR", default=None)

    model_config = ConfigDict(populate_by_name=True)


class AccountEvent(BaseModel):
    event_id: str
    account: AccountAddress
    timestamp: int
    actions: list[Action]
    is_scam: bool
    lt: int
    in_progress: bool
    extra: int
    progress: float
    ext_msg_hash: str | None = Field(default=None)


class AccountEvents(BaseModel):
    events: list[AccountEvent]
    next_from: int


class Accounts(BaseModel):
    accounts: list[Account]


class DefiLockedAsset(BaseModel):
    type: str
    jetton: JettonPreview | None = Field(default=None)


class DefiProvider(BaseModel):
    name: str
    description: str
    link: str
    icon: str
    card: str
    full: str
    tag: str
    miniapp_link: str | None = Field(default=None)


class DefiAsset(BaseModel):
    type: DefiAssetType
    amount: str
    defi_provider: DefiProvider
    locked_asset: DefiLockedAsset
    pool_address: str | None = Field(default=None)
    asset_address: str | None = Field(default=None)


class DefiAssets(BaseModel):
    assets: list[DefiAsset]


class DefiLiquidPoolAssets(BaseModel):
    asset0: DefiLockedAsset
    asset1: DefiLockedAsset


class DnsExpiring(BaseModel):
    items: list[t.Any]


class DomainNames(BaseModel):
    domains: list[str]


class ExecGetMethodArg(BaseModel):
    type: ExecGetMethodArgType
    value: str


class ExtraCurrencies(BaseModel):
    extra_currencies: list[EcPreview]


class FoundAccounts(BaseModel):
    addresses: list[t.Any]


class JettonAssetInfo(BaseModel):
    token_type: DefiAssetType
    defi_provider: DefiProvider
    type: DefiAssetType | None = Field(default=None)
    pool_assets: DefiLiquidPoolAssets | None = Field(default=None)


class JettonBalance(BaseModel):
    balance: str
    wallet_address: AccountAddress
    jetton: JettonPreview
    price: TokenRates | None = Field(default=None)
    defi_asset: JettonAssetInfo | None = Field(default=None)
    extensions: list[str] | None = Field(default=None)
    lock: t.Any | None = Field(default=None)


class JettonOperation(BaseModel):
    operation: str
    utime: int
    lt: int
    transaction_hash: str
    amount: str
    jetton: JettonPreview
    trace_id: str
    query_id: str
    source: AccountAddress | None = Field(default=None)
    destination: AccountAddress | None = Field(default=None)
    payload: t.Any | None = Field(default=None)


class JettonOperations(BaseModel):
    operations: list[JettonOperation]
    next_from: int | None = Field(default=None)


class JettonsBalances(BaseModel):
    balances: list[JettonBalance]


class Multisigs(BaseModel):
    multisigs: list[Multisig]


class Subscription(BaseModel):
    type: str
    status: str
    period: int
    subscription_id: str
    payment_per_period: Price
    wallet: AccountAddress
    next_charge_at: int
    metadata: Metadata
    address: str | None = Field(default=None)
    beneficiary: AccountAddress | None = Field(default=None)
    admin: AccountAddress | None = Field(default=None)


class Subscriptions(BaseModel):
    subscriptions: list[Subscription]


class TraceID(BaseModel):
    id: str
    utime: int


class TraceIDs(BaseModel):
    traces: list[TraceID]

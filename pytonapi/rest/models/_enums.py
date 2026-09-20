# This file is auto-generated. Do not edit manually.

from enum import Enum


class AccStatusChange(str, Enum):
    acst_unchanged = "acst_unchanged"
    acst_frozen = "acst_frozen"
    acst_deleted = "acst_deleted"


class AccountStatus(str, Enum):
    nonexist = "nonexist"
    uninit = "uninit"
    active = "active"
    frozen = "frozen"


class BouncePhaseType(str, Enum):
    TrPhaseBounceNegfunds = "TrPhaseBounceNegfunds"
    TrPhaseBounceNofunds = "TrPhaseBounceNofunds"
    TrPhaseBounceOk = "TrPhaseBounceOk"


class ComputeSkipReason(str, Enum):
    cskip_no_state = "cskip_no_state"
    cskip_bad_state = "cskip_bad_state"
    cskip_no_gas = "cskip_no_gas"
    cskip_suspended = "cskip_suspended"


class CurrencyType(str, Enum):
    native = "native"
    extra_currency = "extra_currency"
    jetton = "jetton"
    fiat = "fiat"


class DefiAssetType(str, Enum):
    staking = "staking"
    lending_supply = "lending_supply"
    lending_borrow = "lending_borrow"
    liquid_staking = "liquid_staking"
    liquid_pool = "liquid_pool"
    yield_token = "yield_token"


class ExecGetMethodArgType(str, Enum):
    nan = "nan"
    null = "null"
    tinyint = "tinyint"
    int257 = "int257"
    slice = "slice"
    cell_boc_base64 = "cell_boc_base64"
    slice_boc_hex = "slice_boc_hex"


class JettonVerificationType(str, Enum):
    whitelist = "whitelist"
    graylist = "graylist"
    blacklist = "blacklist"
    none = "none"


class PoolImplementationType(str, Enum):
    whales = "whales"
    tf = "tf"
    liquidTF = "liquidTF"
    ffvault = "ffvault"
    hipo = "hipo"


class TransactionType(str, Enum):
    TransOrd = "TransOrd"
    TransTickTock = "TransTickTock"
    TransSplitPrepare = "TransSplitPrepare"
    TransSplitInstall = "TransSplitInstall"
    TransMergePrepare = "TransMergePrepare"
    TransMergeInstall = "TransMergeInstall"
    TransStorage = "TransStorage"


class TrustType(str, Enum):
    whitelist = "whitelist"
    graylist = "graylist"
    blacklist = "blacklist"
    none = "none"

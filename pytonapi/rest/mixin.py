# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pytonapi.rest.resources.accounts import AccountsResource
from pytonapi.rest.resources.blockchain import BlockchainResource
from pytonapi.rest.resources.connect import ConnectResource
from pytonapi.rest.resources.dns import DNSResource
from pytonapi.rest.resources.emulation import EmulationResource
from pytonapi.rest.resources.events import EventsResource
from pytonapi.rest.resources.extra_currency import ExtraCurrencyResource
from pytonapi.rest.resources.gasless import GaslessResource
from pytonapi.rest.resources.jettons import JettonsResource
from pytonapi.rest.resources.lite_server import LiteServerResource
from pytonapi.rest.resources.migration import MigrationResource
from pytonapi.rest.resources.multisig import MultisigResource
from pytonapi.rest.resources.nft import NFTResource
from pytonapi.rest.resources.purchases import PurchasesResource
from pytonapi.rest.resources.rates import RatesResource
from pytonapi.rest.resources.rewards import RewardsResource
from pytonapi.rest.resources.staking import StakingResource
from pytonapi.rest.resources.storage import StorageResource
from pytonapi.rest.resources.traces import TracesResource
from pytonapi.rest.resources.utilities import UtilitiesResource
from pytonapi.rest.resources.wallet import WalletResource

if t.TYPE_CHECKING:
    from pytonapi.rest.client import TonapiRestClient


class ResourcesMixin:
    """Mixin that exposes all API resources as properties."""

    def __init__(self, client: TonapiRestClient) -> None:
        self._client = client
        self.accounts = AccountsResource(client)
        self.blockchain = BlockchainResource(client)
        self.connect = ConnectResource(client)
        self.dns = DNSResource(client)
        self.emulation = EmulationResource(client)
        self.events = EventsResource(client)
        self.extra_currency = ExtraCurrencyResource(client)
        self.gasless = GaslessResource(client)
        self.jettons = JettonsResource(client)
        self.lite_server = LiteServerResource(client)
        self.migration = MigrationResource(client)
        self.multisig = MultisigResource(client)
        self.nft = NFTResource(client)
        self.purchases = PurchasesResource(client)
        self.rates = RatesResource(client)
        self.rewards = RewardsResource(client)
        self.staking = StakingResource(client)
        self.storage = StorageResource(client)
        self.traces = TracesResource(client)
        self.utilities = UtilitiesResource(client)
        self.wallet = WalletResource(client)

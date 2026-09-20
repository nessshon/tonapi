# This file is auto-generated. Do not edit manually.

from pytonapi.rest.models import (
    Account,
    AccountEvent,
    AccountEvents,
    Accounts,
    DefiAssets,
    DnsExpiring,
    DomainNames,
    FoundAccounts,
    JettonBalance,
    JettonOperations,
    JettonsBalances,
    Multisigs,
    NftItems,
    Subscriptions,
    TraceIDs,
)
from tests.conftest import TestTonapiRest
from tests.rest.fixtures import params


class TestAccountsResource(TestTonapiRest):
    async def test_get_accounts(self):
        p = params("accounts.get_accounts")
        response = await self.tonapi.accounts.get_accounts(
            body=p["body"],
        )
        self.assertIsInstance(response, Accounts)

    async def test_get_account(self):
        p = params("accounts.get_account")
        response = await self.tonapi.accounts.get_account(
            p["account_id"],
        )
        self.assertIsInstance(response, Account)

    async def test_account_dns_back_resolve(self):
        p = params("accounts.account_dns_back_resolve")
        response = await self.tonapi.accounts.account_dns_back_resolve(
            p["account_id"],
        )
        self.assertIsInstance(response, DomainNames)

    async def test_get_account_jettons_balances(self):
        p = params("accounts.get_account_jettons_balances")
        response = await self.tonapi.accounts.get_account_jettons_balances(
            p["account_id"],
        )
        self.assertIsInstance(response, JettonsBalances)

    async def test_get_account_jetton_balance(self):
        p = params("accounts.get_account_jetton_balance")
        response = await self.tonapi.accounts.get_account_jetton_balance(
            p["account_id"],
            p["jetton_id"],
        )
        self.assertIsInstance(response, JettonBalance)

    async def test_get_account_jettons_history(self):
        p = params("accounts.get_account_jettons_history")
        response = await self.tonapi.accounts.get_account_jettons_history(
            p["account_id"],
            p["limit"],
        )
        self.assertIsInstance(response, JettonOperations)

    async def test_get_account_jetton_history_by_id(self):
        p = params("accounts.get_account_jetton_history_by_id")
        response = await self.tonapi.accounts.get_account_jetton_history_by_id(
            p["account_id"],
            p["jetton_id"],
            p["limit"],
        )
        self.assertIsInstance(response, AccountEvents)

    async def test_get_account_nft_items(self):
        p = params("accounts.get_account_nft_items")
        response = await self.tonapi.accounts.get_account_nft_items(
            p["account_id"],
        )
        self.assertIsInstance(response, NftItems)

    async def test_get_account_events(self):
        p = params("accounts.get_account_events")
        response = await self.tonapi.accounts.get_account_events(
            p["account_id"],
            p["limit"],
        )
        self.assertIsInstance(response, AccountEvents)

    async def test_get_account_event(self):
        p = params("accounts.get_account_event")
        response = await self.tonapi.accounts.get_account_event(
            p["account_id"],
            p["event_id"],
        )
        self.assertIsInstance(response, AccountEvent)

    async def test_get_account_traces(self):
        p = params("accounts.get_account_traces")
        response = await self.tonapi.accounts.get_account_traces(
            p["account_id"],
        )
        self.assertIsInstance(response, TraceIDs)

    async def test_get_account_subscriptions(self):
        p = params("accounts.get_account_subscriptions")
        response = await self.tonapi.accounts.get_account_subscriptions(
            p["account_id"],
        )
        self.assertIsInstance(response, Subscriptions)

    async def test_reindex_account(self):
        p = params("accounts.reindex_account")
        response = await self.tonapi.accounts.reindex_account(
            p["account_id"],
        )
        self.assertIsNone(response)

    async def test_search_accounts(self):
        p = params("accounts.search_accounts")
        response = await self.tonapi.accounts.search_accounts(
            p["name"],
        )
        self.assertIsInstance(response, FoundAccounts)

    async def test_get_account_dns_expiring(self):
        p = params("accounts.get_account_dns_expiring")
        response = await self.tonapi.accounts.get_account_dns_expiring(
            p["account_id"],
        )
        self.assertIsInstance(response, DnsExpiring)

    async def test_get_account_public_key(self):
        p = params("accounts.get_account_public_key")
        response = await self.tonapi.accounts.get_account_public_key(
            p["account_id"],
        )
        self.assertIsInstance(response, dict)

    async def test_get_account_multisigs(self):
        p = params("accounts.get_account_multisigs")
        response = await self.tonapi.accounts.get_account_multisigs(
            p["account_id"],
        )
        self.assertIsInstance(response, Multisigs)

    async def test_get_account_diff(self):
        p = params("accounts.get_account_diff")
        response = await self.tonapi.accounts.get_account_diff(
            p["account_id"],
            p["start_date"],
            p["end_date"],
        )
        self.assertIsInstance(response, dict)

    async def test_get_account_defi_assets(self):
        p = params("accounts.get_account_defi_assets")
        response = await self.tonapi.accounts.get_account_defi_assets(
            p["account_id"],
        )
        self.assertIsInstance(response, DefiAssets)

    async def test_get_account_extra_currency_history_by_id(self):
        p = params("accounts.get_account_extra_currency_history_by_id")
        response = await self.tonapi.accounts.get_account_extra_currency_history_by_id(
            p["account_id"],
            p["id"],
            p["limit"],
        )
        self.assertIsInstance(response, AccountEvents)

    async def test_get_jetton_account_history_by_id(self):
        p = params("accounts.get_jetton_account_history_by_id")
        response = await self.tonapi.accounts.get_jetton_account_history_by_id(
            p["account_id"],
            p["jetton_id"],
            p["limit"],
        )
        self.assertIsInstance(response, JettonOperations)

    # async def test_emulate_message_to_account_event(self):
    #     p = params("accounts.emulate_message_to_account_event")
    #     response = await self.tonapi.accounts.emulate_message_to_account_event(
    #         p["account_id"],
    #         body=p["body"],
    #     )
    #     self.assertIsInstance(response, AccountEvent)

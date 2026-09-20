# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

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
from pytonapi.rest.resources._base import BaseResource


class AccountsResource(BaseResource):
    """AccountsResource resource group."""

    async def get_accounts(
        self,
        body: dict[str, t.Any],
        currency: str | None = None,
    ) -> Accounts:
        """Get human-friendly information about several accounts without low-level details.

        :param body: Request body.
        :param currency: Currency.
        :return: Accounts
        """
        path = "/v2/accounts/_bulk"
        params = {"currency": currency}
        return await self._request(
            method="POST",
            path=path,
            params=params,
            body=body,
            response_model=Accounts,
        )

    async def get_account(
        self,
        account_id: str,
    ) -> Account:
        """Get human-friendly information about an account without low-level details.

        :param account_id: Account ID.
        :return: Account
        """
        path = f"/v2/accounts/{account_id}"
        return await self._request(
            method="GET",
            path=path,
            response_model=Account,
        )

    async def account_dns_back_resolve(
        self,
        account_id: str,
    ) -> DomainNames:
        """Get account's domains.

        :param account_id: Account ID.
        :return: DomainNames
        """
        path = f"/v2/accounts/{account_id}/dns/backresolve"
        return await self._request(
            method="GET",
            path=path,
            response_model=DomainNames,
        )

    async def get_account_jettons_balances(
        self,
        account_id: str,
        currencies: list[str] | None = None,
        supported_extensions: list[str] | None = None,
        limit: int = 1000,
        offset: int = 0,
    ) -> JettonsBalances:
        """Get all Jettons balances by owner address.

        :param account_id: Account ID.
        :param currencies: Accept gram and all possible fiat currencies, separated by commas.
        :param supported_extensions: Comma separated list supported extensions.
        :param limit: Limit.
        :param offset: Offset.
        :return: JettonsBalances
        """
        path = f"/v2/accounts/{account_id}/jettons"
        params = {
            "currencies": ",".join(currencies) if currencies else None,
            "supported_extensions": ",".join(supported_extensions) if supported_extensions else None,
            "limit": limit,
            "offset": offset,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=JettonsBalances,
        )

    async def get_account_jetton_balance(
        self,
        account_id: str,
        jetton_id: str,
        currencies: list[str] | None = None,
        supported_extensions: list[str] | None = None,
    ) -> JettonBalance:
        """Get Jetton balance by owner address.

        :param account_id: Account ID.
        :param jetton_id: Jetton ID.
        :param currencies: Accept gram and all possible fiat currencies, separated by commas.
        :param supported_extensions: Comma separated list supported extensions.
        :return: JettonBalance
        """
        path = f"/v2/accounts/{account_id}/jettons/{jetton_id}"
        params = {
            "currencies": ",".join(currencies) if currencies else None,
            "supported_extensions": ",".join(supported_extensions) if supported_extensions else None,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=JettonBalance,
        )

    async def get_account_jettons_history(
        self,
        account_id: str,
        limit: int,
        before_lt: int | None = None,
    ) -> JettonOperations:
        """Get the transfer jettons history for account.

        :param account_id: Account ID.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Limit.
        :return: JettonOperations
        """
        path = f"/v2/accounts/{account_id}/jettons/history"
        params = {
            "before_lt": before_lt,
            "limit": limit,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=JettonOperations,
        )

    async def get_account_jetton_history_by_id(
        self,
        account_id: str,
        jetton_id: str,
        limit: int,
        before_lt: int | None = None,
        start_date: int | None = None,
        end_date: int | None = None,
        accept_language: str | None = None,
    ) -> AccountEvents:
        """Please use `getJettonAccountHistoryByID`` instead.

        :param account_id: Account ID.
        :param jetton_id: Jetton ID.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Limit.
        :param start_date: Start date.
        :param end_date: End date.
        :param accept_language: Accept language.
        :return: AccountEvents
        """
        path = f"/v2/accounts/{account_id}/jettons/{jetton_id}/history"
        params = {
            "before_lt": before_lt,
            "limit": limit,
            "start_date": start_date,
            "end_date": end_date,
        }
        headers = {"Accept-Language": accept_language}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            headers=headers,
            response_model=AccountEvents,
        )

    async def get_account_nft_items(
        self,
        account_id: str,
        collection: str | None = None,
        limit: int = 1000,
        offset: int = 0,
        indirect_ownership: bool = False,
    ) -> NftItems:
        """Get all NFT items by owner address.

        :param account_id: Account ID.
        :param collection: Nft collection.
        :param limit: Limit.
        :param offset: Offset.
        :param indirect_ownership: Selling nft items in TON implemented usually via transfer items to special selling
            account. This option enables including items which owned not directly.
        :return: NftItems
        """
        path = f"/v2/accounts/{account_id}/nfts"
        params = {
            "collection": collection,
            "limit": limit,
            "offset": offset,
            "indirect_ownership": indirect_ownership,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=NftItems,
        )

    async def get_account_events(
        self,
        account_id: str,
        limit: int,
        initiator: bool = False,
        subject_only: bool = False,
        after_lt: int | None = None,
        before_lt: int | None = None,
        start_date: int | None = None,
        end_date: int | None = None,
        sort_order: str = "desc",
        accept_language: str | None = None,
    ) -> AccountEvents:
        """Get events for an account. Each event is built on top of a trace which is a series of transactions
        caused by one inbound message. TonAPI looks for known patterns inside the trace and splits the trace
        into actions, where a single action represents a meaningful high-level operation like a Jetton Transfer
        or an NFT Purchase. Actions are expected to be shown to users. It is advised not to build any logic on
        top of actions because actions can be changed at any time.

        :param account_id: Account ID.
        :param initiator: Show only events that are initiated by this account.
        :param subject_only: Filter actions where requested account is not real subject (for example sender or receiver
            jettons).
        :param after_lt: Omit this parameter to get last events.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Limit.
        :param start_date: Start date.
        :param end_date: End date.
        :param sort_order: Sort order.
        :param accept_language: Accept language.
        :return: AccountEvents
        """
        path = f"/v2/accounts/{account_id}/events"
        params = {
            "initiator": initiator,
            "subject_only": subject_only,
            "after_lt": after_lt,
            "before_lt": before_lt,
            "limit": limit,
            "start_date": start_date,
            "end_date": end_date,
            "sort_order": sort_order,
        }
        headers = {"Accept-Language": accept_language}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            headers=headers,
            response_model=AccountEvents,
        )

    async def get_account_event(
        self,
        account_id: str,
        event_id: str,
        subject_only: bool = False,
        accept_language: str | None = None,
    ) -> AccountEvent:
        """Get event for an account by event_id.

        :param account_id: Account ID.
        :param event_id: Event ID or transaction hash in hex (without 0x) or base64url format.
        :param subject_only: Filter actions where requested account is not real subject (for example sender or receiver
            jettons).
        :param accept_language: Accept language.
        :return: AccountEvent
        """
        path = f"/v2/accounts/{account_id}/events/{event_id}"
        params = {"subject_only": subject_only}
        headers = {"Accept-Language": accept_language}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            headers=headers,
            response_model=AccountEvent,
        )

    async def get_account_traces(
        self,
        account_id: str,
        before_lt: int | None = None,
        limit: int = 100,
    ) -> TraceIDs:
        """Get traces for account.

        :param account_id: Account ID.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Limit.
        :return: TraceIDs
        """
        path = f"/v2/accounts/{account_id}/traces"
        params = {
            "before_lt": before_lt,
            "limit": limit,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=TraceIDs,
        )

    async def get_account_subscriptions(
        self,
        account_id: str,
    ) -> Subscriptions:
        """Get all subscriptions by wallet address.

        :param account_id: Account ID.
        :return: Subscriptions
        """
        path = f"/v2/accounts/{account_id}/subscriptions"
        return await self._request(
            method="GET",
            path=path,
            response_model=Subscriptions,
        )

    async def reindex_account(
        self,
        account_id: str,
    ) -> None:
        """Update internal cache for a particular account.

        :param account_id: Account ID.
        """
        path = f"/v2/accounts/{account_id}/reindex"
        await self._request(
            method="POST",
            path=path,
        )

    async def search_accounts(
        self,
        name: str,
    ) -> FoundAccounts:
        """Search by account domain name.

        :param name: Name.
        :return: FoundAccounts
        """
        path = "/v2/accounts/search"
        params = {"name": name}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=FoundAccounts,
        )

    async def get_account_dns_expiring(
        self,
        account_id: str,
        period: int | None = None,
    ) -> DnsExpiring:
        """Get expiring account .ton dns.

        :param account_id: Account ID.
        :param period: Number of days before expiration.
        :return: DnsExpiring
        """
        path = f"/v2/accounts/{account_id}/dns/expiring"
        params = {"period": period}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=DnsExpiring,
        )

    async def get_account_public_key(
        self,
        account_id: str,
    ) -> t.Any:
        """Get public key by account id.

        :param account_id: Account ID.
        :return: dict[str, t.Any]
        """
        path = f"/v2/accounts/{account_id}/publickey"
        return await self._request(
            method="GET",
            path=path,
        )

    async def get_account_multisigs(
        self,
        account_id: str,
    ) -> Multisigs:
        """Get account's multisigs.

        :param account_id: Account ID.
        :return: Multisigs
        """
        path = f"/v2/accounts/{account_id}/multisigs"
        return await self._request(
            method="GET",
            path=path,
            response_model=Multisigs,
        )

    async def get_account_diff(
        self,
        account_id: str,
        start_date: int,
        end_date: int,
    ) -> t.Any:
        """Get account's balance change.

        :param account_id: Account ID.
        :param start_date: Start date.
        :param end_date: End date.
        :return: dict[str, t.Any]
        """
        path = f"/v2/accounts/{account_id}/diff"
        params = {
            "start_date": start_date,
            "end_date": end_date,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
        )

    async def get_account_defi_assets(
        self,
        account_id: str,
    ) -> DefiAssets:
        """Return DeFi assets locked in custom smart contracts: currently returns TON Whales staking and EVAA
        lending positions.

        :param account_id: Account ID.
        :return: DefiAssets
        """
        path = f"/v2/accounts/{account_id}/defi/assets"
        return await self._request(
            method="GET",
            path=path,
            response_model=DefiAssets,
        )

    async def get_account_extra_currency_history_by_id(
        self,
        account_id: str,
        id: int,
        limit: int,
        before_lt: int | None = None,
        start_date: int | None = None,
        end_date: int | None = None,
        accept_language: str | None = None,
    ) -> AccountEvents:
        """Get the transfer history of extra currencies for an account.

        :param account_id: Account ID.
        :param id: Extra currency id.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Limit.
        :param start_date: Start date.
        :param end_date: End date.
        :param accept_language: Accept language.
        :return: AccountEvents
        """
        path = f"/v2/accounts/{account_id}/extra-currency/{id}/history"
        params = {
            "before_lt": before_lt,
            "limit": limit,
            "start_date": start_date,
            "end_date": end_date,
        }
        headers = {"Accept-Language": accept_language}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            headers=headers,
            response_model=AccountEvents,
        )

    async def get_jetton_account_history_by_id(
        self,
        account_id: str,
        jetton_id: str,
        limit: int,
        before_lt: int | None = None,
        start_date: int | None = None,
        end_date: int | None = None,
    ) -> JettonOperations:
        """Get the transfer jetton history for account and jetton.

        :param account_id: Account ID.
        :param jetton_id: Jetton ID.
        :param before_lt: Omit this parameter to get last events.
        :param limit: Limit.
        :param start_date: Start date.
        :param end_date: End date.
        :return: JettonOperations
        """
        path = f"/v2/jettons/{jetton_id}/accounts/{account_id}/history"
        params = {
            "before_lt": before_lt,
            "limit": limit,
            "start_date": start_date,
            "end_date": end_date,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=JettonOperations,
        )

    async def emulate_message_to_account_event(
        self,
        account_id: str,
        body: dict[str, t.Any],
        ignore_signature_check: bool | None = None,
        accept_language: str | None = None,
    ) -> AccountEvent:
        """Emulate sending message to retrieve account-specific events.

        :param account_id: Account ID.
        :param body: Request body.
        :param ignore_signature_check: Ignore signature check.
        :param accept_language: Accept language.
        :return: AccountEvent
        """
        path = f"/v2/accounts/{account_id}/events/emulate"
        params = {"ignore_signature_check": ignore_signature_check}
        headers = {"Accept-Language": accept_language}
        return await self._request(
            method="POST",
            path=path,
            params=params,
            body=body,
            headers=headers,
            response_model=AccountEvent,
        )

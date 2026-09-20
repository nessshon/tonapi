# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pytonapi.rest.models import MigrationPrepareRequest, MigrationPrepareResponse, MigrationWallets
from pytonapi.rest.resources._base import BaseResource


class MigrationResource(BaseResource):
    """MigrationResource resource group."""

    async def get_wallets(
        self,
        body: dict[str, t.Any],
        currencies: list[str] | None = None,
    ) -> MigrationWallets:
        """Get migratable assets value (TON balance, jettons with prices, NFT count) for several wallets at once.

        :param body: Request body.
        :param currencies: Accept gram and all possible fiat currencies, separated by commas.
        :return: MigrationWallets
        """
        path = "/v2/migration/wallets"
        params = {"currencies": ",".join(currencies) if currencies else None}
        return await self._request(
            method="POST",
            path=path,
            params=params,
            body=body,
            response_model=MigrationWallets,
        )

    async def prepare_migration(
        self,
        body: MigrationPrepareRequest,
    ) -> MigrationPrepareResponse:
        """Prepare ordered signable transactions that migrate every asset from `from` to `to`.

        :param body: Request body.
        :return: MigrationPrepareResponse
        """
        path = "/v2/migration/prepare"
        return await self._request(
            method="POST",
            path=path,
            body=body.model_dump(by_alias=True, exclude_none=True),
            response_model=MigrationPrepareResponse,
        )

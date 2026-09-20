# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pytonapi.rest.resources._base import BaseResource


class RatesResource(BaseResource):
    """RatesResource resource group."""

    async def get_rates(
        self,
        tokens: list[str],
        currencies: list[str],
    ) -> t.Any:
        """Get the token price in the chosen currency for display only. Don't use this for financial transactions.

        :param tokens: Accept gram and jetton master addresses, separated by commas.
        :param currencies: Accept gram and all possible fiat currencies, separated by commas.
        :return: dict[str, t.Any]
        """
        path = "/v2/rates"
        params = {
            "tokens": ",".join(tokens),
            "currencies": ",".join(currencies),
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
        )

    async def get_chart_rates(
        self,
        token: str,
        currency: str | None = None,
        start_date: int | None = None,
        end_date: int | None = None,
        points_count: int = 200,
    ) -> t.Any:
        """Get chart by token.

        :param token: Accept jetton master address.
        :param currency: Currency.
        :param start_date: Start date.
        :param end_date: End date.
        :param points_count: Points count.
        :return: dict[str, t.Any]
        """
        path = "/v2/rates/chart"
        params = {
            "token": token,
            "currency": currency,
            "start_date": start_date,
            "end_date": end_date,
            "points_count": points_count,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
        )

    async def get_markets_rates(
        self,
    ) -> t.Any:
        """Get the Gram price from markets.

        :return: dict[str, t.Any]
        """
        path = "/v2/rates/markets"
        return await self._request(
            method="GET",
            path=path,
        )

# This file is auto-generated. Do not edit manually.

from __future__ import annotations

from pytonapi.rest.models import RewardsStats, RoundRewardsResponse, ValidationRoundsResponse, ValidatorsResponse
from pytonapi.rest.resources._base import BaseResource


class RewardsResource(BaseResource):
    """RewardsResource resource group."""

    async def get_validators(
        self,
        seqno: int | None = None,
        unixtime: int | None = None,
        shallow: bool = False,
    ) -> ValidatorsResponse:
        """Return all current validators with stakes, rewards, pool addresses, and (optionally) nominator breakdowns.

        :param seqno: Masterchain block seqno. Defaults to latest. Mutually exclusive with `unixtime`.
        :param unixtime: Unix timestamp (seconds). Looks up the masterchain block at this time and uses it as the
            anchor. Mutually exclusive with `seqno`.
        :param shallow: Set to `1` to return only basic validator info (rank, pubkey, effective_stake, weight, reward,
            pool). Skips pool type detection, owner/validator addresses, nominator data, and returned-stake lookup —
            significantly faster.
        :return: ValidatorsResponse
        """
        path = "/v2/rewards/validators"
        params = {
            "seqno": seqno,
            "unixtime": unixtime,
            "shallow": shallow,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=ValidatorsResponse,
        )

    async def get_validation_rounds(
        self,
        election_id: int | None = None,
        block: int | None = None,
        unixtime: int | None = None,
    ) -> ValidationRoundsResponse:
        """Return past and current validation rounds with boundaries, stakes, and bonuses. Always uses the
        latest masterchain block.

        :param election_id: Return the single round matching this election ID. Mutually exclusive with `block` and
            `unixtime`.
        :param block: Find the round containing this masterchain block seqno and return it plus up to `limit-1` older
            rounds. Mutually exclusive with `election_id` and `unixtime`.
        :param unixtime: Unix timestamp (seconds). Looks up the masterchain block at this time and uses it as the
            anchor. Mutually exclusive with `election_id` and `block`.
        :return: ValidationRoundsResponse
        """
        path = "/v2/rewards/validation-rounds"
        params = {
            "election_id": election_id,
            "block": block,
            "unixtime": unixtime,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=ValidationRoundsResponse,
        )

    async def get_round_rewards(
        self,
        election_id: int | None = None,
        block: int | None = None,
        unixtime: int | None = None,
        shallow: bool = False,
    ) -> RoundRewardsResponse:
        """Compute per-validator and per-nominator reward distribution for a finished validation round using the
        elector's bonuses value.

        :param election_id: Election ID of the finished round. Mutually exclusive with `block` and `unixtime`.
        :param block: Masterchain block seqno within the finished round. Mutually exclusive with `election_id` and
            `unixtime`.
        :param unixtime: Unix timestamp (seconds). Looks up the masterchain block at this time and uses it as the
            anchor. Mutually exclusive with `election_id` and `block`.
        :param shallow: Set to `1` to return only basic validator info (rank, pubkey, effective_stake, weight, reward,
            pool). Skips pool type detection, owner/validator addresses, nominator data, and returned-stake lookup —
            significantly faster.
        :return: RoundRewardsResponse
        """
        path = "/v2/rewards/round-rewards"
        params = {
            "election_id": election_id,
            "block": block,
            "unixtime": unixtime,
            "shallow": shallow,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=RoundRewardsResponse,
        )

    async def get_stats(
        self,
    ) -> RewardsStats:
        """Return time series of APY and total stake from past validation rounds.

        :return: RewardsStats
        """
        path = "/v2/rewards/stats"
        return await self._request(
            method="GET",
            path=path,
            response_model=RewardsStats,
        )

    async def get_apy(
        self,
    ) -> float:
        """Return the current TON blockchain APY as a percent based on the latest completed validation round.

        :return: float
        """
        path = "/v2/rewards/apy"
        return await self._request(
            method="GET",
            path=path,
            response_model=float,
        )

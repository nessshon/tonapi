# This file is auto-generated. Do not edit manually.

from pytonapi.rest.models import RewardsStats, ValidationRoundsResponse, ValidatorsResponse
from tests.conftest import TestTonapiRest


class TestRewardsResource(TestTonapiRest):
    async def test_get_validators(self):
        response = await self.tonapi.rewards.get_validators()
        self.assertIsInstance(response, ValidatorsResponse)

    async def test_get_validation_rounds(self):
        response = await self.tonapi.rewards.get_validation_rounds()
        self.assertIsInstance(response, ValidationRoundsResponse)

    # async def test_get_round_rewards(self):
    #     response = await self.tonapi.rewards.get_round_rewards()
    #     self.assertIsInstance(response, RoundRewardsResponse)

    async def test_get_stats(self):
        response = await self.tonapi.rewards.get_stats()
        self.assertIsInstance(response, RewardsStats)

    async def test_get_apy(self):
        response = await self.tonapi.rewards.get_apy()
        self.assertIsInstance(response, float)

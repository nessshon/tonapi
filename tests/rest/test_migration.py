# This file is auto-generated. Do not edit manually.

from pytonapi.rest.models import MigrationWallets
from tests.conftest import TestTonapiRest
from tests.rest.fixtures import params


class TestMigrationResource(TestTonapiRest):
    async def test_get_wallets(self):
        p = params("migration.get_wallets")
        response = await self.tonapi.migration.get_wallets(
            body=p["body"],
        )
        self.assertIsInstance(response, MigrationWallets)

    # async def test_prepare_migration(self):
    #     p = params("migration.prepare_migration")
    #     response = await self.tonapi.migration.prepare_migration(
    #         body=p["body"],
    #     )
    #     self.assertIsInstance(response, MigrationPrepareResponse)

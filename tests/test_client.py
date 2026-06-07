from unittest import IsolatedAsyncioTestCase

import aiohttp

from pytonapi.exceptions import TONAPISessionNotCreatedError
from pytonapi.rest import TonapiRestClient


class TestSessionProperty(IsolatedAsyncioTestCase):
    async def test_raises_before_create_session(self) -> None:
        client = TonapiRestClient()
        with self.assertRaises(TONAPISessionNotCreatedError):
            _ = client.session

    async def test_returns_active_session(self) -> None:
        client = TonapiRestClient()
        await client.create_session()
        try:
            self.assertIsInstance(client.session, aiohttp.ClientSession)
        finally:
            await client.close_session()

    async def test_raises_after_close(self) -> None:
        client = TonapiRestClient()
        await client.create_session()
        await client.close_session()
        with self.assertRaises(TONAPISessionNotCreatedError):
            _ = client.session

    async def test_available_in_context_manager(self) -> None:
        async with TonapiRestClient() as client:
            self.assertIsInstance(client.session, aiohttp.ClientSession)

from unittest import IsolatedAsyncioTestCase

from pytonapi.exceptions import TONAPIError
from pytonapi.webhook import (
    AccountTxEvent,
    MempoolMsgEvent,
    NewContractsEvent,
    OpcodeMsgEvent,
    TonapiWebhookDispatcher,
)


class TestTonapiWebhookDispatcher(IsolatedAsyncioTestCase):
    @staticmethod
    def _make_account_tx_data(
        account_id: str = "0:abc",
        lt: int = 100,
        tx_hash: str = "deadbeef",
    ) -> dict:
        return {
            "event_type": "account_tx",
            "account_id": account_id,
            "lt": lt,
            "tx_hash": tx_hash,
        }

    @staticmethod
    def _make_mempool_msg_data(boc: str = "te6cc...") -> dict:
        return {
            "event_type": "mempool_msg",
            "boc": boc,
        }

    @staticmethod
    def _make_opcode_msg_data(
        account_id: str = "0:abc",
        lt: int = 100,
        tx_hash: str = "deadbeef",
    ) -> dict:
        return {
            "event_type": "opcode_msg",
            "account_id": account_id,
            "lt": lt,
            "tx_hash": tx_hash,
        }

    @staticmethod
    def _make_new_contracts_data(
        account_id: str = "0:abc",
        lt: int = 100,
        tx_hash: str = "deadbeef",
    ) -> dict:
        return {
            "event_type": "new_contracts",
            "account_id": account_id,
            "lt": lt,
            "tx_hash": tx_hash,
        }

    async def test_all_event_types_dispatch(self) -> None:
        dispatcher = TonapiWebhookDispatcher()
        tx, mempool, opcode, nc = [], [], [], []

        @dispatcher.account_tx()
        async def h1(event: AccountTxEvent) -> None:
            tx.append(event)

        @dispatcher.mempool_msg()
        async def h2(event: MempoolMsgEvent) -> None:
            mempool.append(event)

        @dispatcher.opcode_msg()
        async def h3(event: OpcodeMsgEvent) -> None:
            opcode.append(event)

        @dispatcher.new_contracts()
        async def h4(event: NewContractsEvent) -> None:
            nc.append(event)

        await dispatcher.process("/account-tx", self._make_account_tx_data())
        await dispatcher.process("/mempool-msg", self._make_mempool_msg_data())
        await dispatcher.process("/opcode-msg", self._make_opcode_msg_data())
        await dispatcher.process("/new-contracts", self._make_new_contracts_data())

        self.assertEqual(len(tx), 1)
        self.assertIsInstance(tx[0], AccountTxEvent)
        self.assertEqual(tx[0].account_id, "0:abc")

        self.assertEqual(len(mempool), 1)
        self.assertIsInstance(mempool[0], MempoolMsgEvent)
        self.assertEqual(mempool[0].boc, "te6cc...")

        self.assertEqual(len(opcode), 1)
        self.assertEqual(len(nc), 1)

    async def test_multiple_handlers(self) -> None:
        dispatcher = TonapiWebhookDispatcher()
        a, b = [], []

        @dispatcher.account_tx()
        async def handler_a(event: AccountTxEvent) -> None:
            a.append(event)

        @dispatcher.account_tx()
        async def handler_b(event: AccountTxEvent) -> None:
            b.append(event)

        await dispatcher.process("/account-tx", self._make_account_tx_data())

        self.assertEqual(len(a), 1)
        self.assertEqual(len(b), 1)

    async def test_account_filter(self) -> None:
        dispatcher = TonapiWebhookDispatcher()
        filtered, all_events = [], []

        @dispatcher.account_tx("0:target")
        async def filtered_handler(event: AccountTxEvent) -> None:
            filtered.append(event)

        @dispatcher.account_tx()
        async def catch_all(event: AccountTxEvent) -> None:
            all_events.append(event)

        await dispatcher.process("/account-tx", self._make_account_tx_data(account_id="0:target"))
        await dispatcher.process("/account-tx", self._make_account_tx_data(account_id="0:other"))

        self.assertEqual(len(filtered), 1)
        self.assertEqual(len(all_events), 2)

    async def test_custom_path(self) -> None:
        dispatcher = TonapiWebhookDispatcher()
        received = []

        @dispatcher.account_tx(path="/my-custom-tx")
        async def handler(event: AccountTxEvent) -> None:
            received.append(event)

        await dispatcher.process("/my-custom-tx", self._make_account_tx_data())

        self.assertEqual(len(received), 1)

    async def test_unknown_path_raises_error(self) -> None:
        dispatcher = TonapiWebhookDispatcher()

        @dispatcher.account_tx()
        async def handler(event: AccountTxEvent) -> None:
            pass

        with self.assertRaises(TONAPIError):
            await dispatcher.process("/unknown", self._make_account_tx_data())

    async def test_dependency_injection(self) -> None:
        dispatcher = TonapiWebhookDispatcher(db="fake_db")
        received = []

        @dispatcher.account_tx()
        async def handler(event: AccountTxEvent, db: str) -> None:
            received.append(db)

        await dispatcher.process("/account-tx", self._make_account_tx_data())

        self.assertEqual(received, ["fake_db"])

        # process kwargs override constructor defaults
        await dispatcher.process("/account-tx", self._make_account_tx_data(), db="override")

        self.assertEqual(received[-1], "override")

    async def test_sync_handler(self) -> None:
        dispatcher = TonapiWebhookDispatcher()
        received = []

        @dispatcher.account_tx()
        def handler(event: AccountTxEvent) -> None:
            received.append(event)

        await dispatcher.process("/account-tx", self._make_account_tx_data())

        self.assertEqual(len(received), 1)

    async def test_token_validation(self) -> None:
        dispatcher = TonapiWebhookDispatcher()
        received = []

        @dispatcher.account_tx()
        async def handler(event: AccountTxEvent) -> None:
            received.append(event)

        dispatcher._tokens["/account-tx"] = "my-secret"

        # Valid token
        await dispatcher.process(
            "/account-tx",
            self._make_account_tx_data(),
            authorization="Bearer my-secret",
        )
        self.assertEqual(len(received), 1)

        # Invalid token
        with self.assertRaises(TONAPIError):
            await dispatcher.process(
                "/account-tx",
                self._make_account_tx_data(),
                authorization="Bearer wrong",
            )

        # Missing token
        with self.assertRaises(TONAPIError):
            await dispatcher.process("/account-tx", self._make_account_tx_data())

    async def test_setup_enforces_auth_on_custom_path(self) -> None:
        class _FakeWebhook:
            def __init__(self, token: str, endpoint: str) -> None:
                self.token = token
                self.endpoint = endpoint

            async def sync_accounts(self, accounts: list) -> None:
                pass

        class _FakeClient:
            def __init__(self) -> None:
                self.endpoints: list[str] = []

            async def create_session(self) -> None:
                pass

            async def ensure(self, endpoint: str) -> "_FakeWebhook":
                self.endpoints.append(endpoint)
                return _FakeWebhook("secret-token", endpoint)

            async def close_session(self) -> None:
                pass

        client = _FakeClient()
        dispatcher = TonapiWebhookDispatcher(
            "https://victim.example/hook",
            client=client,  # type: ignore[arg-type]
            accounts=["0:victim"],
        )
        received = []

        @dispatcher.account_tx("0:victim", path="/hook/custom")
        async def handler(event: AccountTxEvent) -> None:
            received.append(event.tx_hash)

        await dispatcher.setup()

        # The custom path must be registered with TONAPI and have a stored token.
        self.assertIn("/hook/custom", dispatcher._tokens)
        self.assertIn("https://victim.example/hook/custom", client.endpoints)

        data = self._make_account_tx_data(account_id="0:victim")

        # Missing auth must be rejected.
        with self.assertRaises(TONAPIError):
            await dispatcher.process("/hook/custom", data)

        # Wrong auth must be rejected.
        with self.assertRaises(TONAPIError):
            await dispatcher.process("/hook/custom", data, authorization="Bearer wrong")

        # Valid auth is accepted.
        await dispatcher.process("/hook/custom", data, authorization="Bearer secret-token")
        self.assertEqual(received, ["deadbeef"])

    async def test_register_invalid_event_key(self) -> None:
        dispatcher = TonapiWebhookDispatcher()

        async def handler(event) -> None:
            pass

        with self.assertRaises(ValueError):
            dispatcher.register("invalid_key", handler)  # type: ignore[arg-type]

# This file is auto-generated. Do not edit manually.

from pytonapi.rest.models import (
    BlockchainAccountInspect,
    BlockchainBlock,
    BlockchainBlocks,
    BlockchainBlockShards,
    BlockchainConfig,
    BlockchainRawAccount,
    BlockchainRawAccounts,
    MethodExecutionResult,
    RawBlockchainConfig,
    ReducedBlocks,
    Transaction,
    Transactions,
    Validators,
)
from tests.conftest import TestTonapiRest
from tests.rest.fixtures import params


class TestBlockchainResource(TestTonapiRest):
    async def test_get_reduced_blockchain_blocks(self):
        p = params("blockchain.get_reduced_blockchain_blocks")
        response = await self.tonapi.blockchain.get_reduced_blockchain_blocks(
            p["from_"],
            p["to"],
        )
        self.assertIsInstance(response, ReducedBlocks)

    async def test_get_block(self):
        p = params("blockchain.get_block")
        response = await self.tonapi.blockchain.get_block(
            p["block_id"],
        )
        self.assertIsInstance(response, BlockchainBlock)

    async def test_download_blockchain_block_boc(self):
        p = params("blockchain.download_blockchain_block_boc")
        response = await self.tonapi.blockchain.download_blockchain_block_boc(
            p["block_id"],
        )
        self.assertIsInstance(response, bytes)

    async def test_get_masterchain_shards(self):
        p = params("blockchain.get_masterchain_shards")
        response = await self.tonapi.blockchain.get_masterchain_shards(
            p["masterchain_seqno"],
        )
        self.assertIsInstance(response, BlockchainBlockShards)

    async def test_get_masterchain_blocks(self):
        p = params("blockchain.get_masterchain_blocks")
        response = await self.tonapi.blockchain.get_masterchain_blocks(
            p["masterchain_seqno"],
        )
        self.assertIsInstance(response, BlockchainBlocks)

    async def test_get_masterchain_transactions(self):
        p = params("blockchain.get_masterchain_transactions")
        response = await self.tonapi.blockchain.get_masterchain_transactions(
            p["masterchain_seqno"],
        )
        self.assertIsInstance(response, Transactions)

    async def test_get_config_from_block(self):
        p = params("blockchain.get_config_from_block")
        response = await self.tonapi.blockchain.get_config_from_block(
            p["masterchain_seqno"],
        )
        self.assertIsInstance(response, BlockchainConfig)

    async def test_get_raw_blockchain_config_from_block(self):
        p = params("blockchain.get_raw_blockchain_config_from_block")
        response = await self.tonapi.blockchain.get_raw_blockchain_config_from_block(
            p["masterchain_seqno"],
        )
        self.assertIsInstance(response, RawBlockchainConfig)

    async def test_get_block_transactions(self):
        p = params("blockchain.get_block_transactions")
        response = await self.tonapi.blockchain.get_block_transactions(
            p["block_id"],
        )
        self.assertIsInstance(response, Transactions)

    async def test_get_transaction(self):
        p = params("blockchain.get_transaction")
        response = await self.tonapi.blockchain.get_transaction(
            p["transaction_id"],
        )
        self.assertIsInstance(response, Transaction)

    async def test_get_transaction_by_message_hash(self):
        p = params("blockchain.get_transaction_by_message_hash")
        response = await self.tonapi.blockchain.get_transaction_by_message_hash(
            p["msg_id"],
        )
        self.assertIsInstance(response, Transaction)

    async def test_get_validators(self):
        response = await self.tonapi.blockchain.get_validators()
        self.assertIsInstance(response, Validators)

    async def test_get_masterchain_head(self):
        response = await self.tonapi.blockchain.get_masterchain_head()
        self.assertIsInstance(response, BlockchainBlock)

    async def test_get_raw_account(self):
        p = params("blockchain.get_raw_account")
        response = await self.tonapi.blockchain.get_raw_account(
            p["account_id"],
        )
        self.assertIsInstance(response, BlockchainRawAccount)

    async def test_get_raw_accounts(self):
        p = params("blockchain.get_raw_accounts")
        response = await self.tonapi.blockchain.get_raw_accounts(
            body=p["body"],
        )
        self.assertIsInstance(response, BlockchainRawAccounts)

    async def test_get_account_transactions(self):
        p = params("blockchain.get_account_transactions")
        response = await self.tonapi.blockchain.get_account_transactions(
            p["account_id"],
        )
        self.assertIsInstance(response, Transactions)

    async def test_execute_get_method(self):
        p = params("blockchain.execute_get_method")
        response = await self.tonapi.blockchain.execute_get_method(
            p["account_id"],
            p["method_name"],
        )
        self.assertIsInstance(response, MethodExecutionResult)

    async def test_execute_get_method_with_body(self):
        p = params("blockchain.execute_get_method_with_body")
        response = await self.tonapi.blockchain.execute_get_method_with_body(
            p["account_id"],
            p["method_name"],
            body=p["body"],
        )
        self.assertIsInstance(response, MethodExecutionResult)

    # async def test_send_message(self):
    #     p = params("blockchain.send_message")
    #     response = await self.tonapi.blockchain.send_message(
    #         body=p["body"],
    #     )
    #     self.assertIsNone(response)

    async def test_get_config(self):
        response = await self.tonapi.blockchain.get_config()
        self.assertIsInstance(response, BlockchainConfig)

    async def test_get_raw_blockchain_config(self):
        response = await self.tonapi.blockchain.get_raw_blockchain_config()
        self.assertIsInstance(response, RawBlockchainConfig)

    async def test_account_inspect(self):
        p = params("blockchain.account_inspect")
        response = await self.tonapi.blockchain.account_inspect(
            p["account_id"],
        )
        self.assertIsInstance(response, BlockchainAccountInspect)

    # async def test_get_library_by_hash(self):
    #     p = params("blockchain.get_library_by_hash")
    #     response = await self.tonapi.blockchain.get_library_by_hash(
    #         p["hash"],
    #     )
    #     self.assertIsInstance(response, BlockchainLibrary)

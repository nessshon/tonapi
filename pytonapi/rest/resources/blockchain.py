# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pytonapi.rest.models import (
    BlockchainAccountInspect,
    BlockchainBlock,
    BlockchainBlocks,
    BlockchainBlockShards,
    BlockchainConfig,
    BlockchainLibrary,
    BlockchainRawAccount,
    BlockchainRawAccounts,
    MethodExecutionResult,
    RawBlockchainConfig,
    ReducedBlocks,
    Transaction,
    Transactions,
    Validators,
)
from pytonapi.rest.resources._base import BaseResource


class BlockchainResource(BaseResource):
    """BlockchainResource resource group."""

    async def get_reduced_blockchain_blocks(
        self,
        from_: int,
        to: int,
    ) -> ReducedBlocks:
        """Get reduced blockchain blocks data.

        :param from_: From.
        :param to: To.
        :return: ReducedBlocks
        """
        path = "/v2/blockchain/reduced/blocks"
        params = {
            "from": from_,
            "to": to,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=ReducedBlocks,
        )

    async def get_block(
        self,
        block_id: str,
    ) -> BlockchainBlock:
        """Get blockchain block data.

        :param block_id: Block ID.
        :return: BlockchainBlock
        """
        path = f"/v2/blockchain/blocks/{block_id}"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainBlock,
        )

    async def download_blockchain_block_boc(
        self,
        block_id: str,
    ) -> bytes:
        """Download blockchain block BOC.

        :param block_id: Block ID.
        :return: bytes
        """
        path = f"/v2/blockchain/blocks/{block_id}/boc"
        return await self._request(
            method="GET",
            path=path,
            response_model=bytes,
        )

    async def get_masterchain_shards(
        self,
        masterchain_seqno: int,
    ) -> BlockchainBlockShards:
        """Get blockchain block shards.

        :param masterchain_seqno: Masterchain block seqno.
        :return: BlockchainBlockShards
        """
        path = f"/v2/blockchain/masterchain/{masterchain_seqno}/shards"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainBlockShards,
        )

    async def get_masterchain_blocks(
        self,
        masterchain_seqno: int,
    ) -> BlockchainBlocks:
        """Get all blocks in all shards and workchains between target and previous masterchain block according
        to shards last blocks snapshot in masterchain.  We don't recommend to build your app around this method
        because it has problem with scalability and will work very slow in the future.

        :param masterchain_seqno: Masterchain block seqno.
        :return: BlockchainBlocks
        """
        path = f"/v2/blockchain/masterchain/{masterchain_seqno}/blocks"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainBlocks,
        )

    async def get_masterchain_transactions(
        self,
        masterchain_seqno: int,
        offset: int = 0,
        limit: int | None = None,
    ) -> Transactions:
        """Get all transactions in all shards and workchains between target and previous masterchain block
        according to shards last blocks snapshot in masterchain. We don't recommend to build your app around
        this method because it has problem with scalability and will work very slow in the future.

        :param masterchain_seqno: Masterchain block seqno.
        :param offset: Offset.
        :param limit: Limit.
        :return: Transactions
        """
        path = f"/v2/blockchain/masterchain/{masterchain_seqno}/transactions"
        params = {
            "offset": offset,
            "limit": limit,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=Transactions,
        )

    async def get_config_from_block(
        self,
        masterchain_seqno: int,
    ) -> BlockchainConfig:
        """Get blockchain config from a specific block, if present.

        :param masterchain_seqno: Masterchain block seqno.
        :return: BlockchainConfig
        """
        path = f"/v2/blockchain/masterchain/{masterchain_seqno}/config"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainConfig,
        )

    async def get_raw_blockchain_config_from_block(
        self,
        masterchain_seqno: int,
    ) -> RawBlockchainConfig:
        """Get raw blockchain config from a specific block, if present.

        :param masterchain_seqno: Masterchain block seqno.
        :return: RawBlockchainConfig
        """
        path = f"/v2/blockchain/masterchain/{masterchain_seqno}/config/raw"
        return await self._request(
            method="GET",
            path=path,
            response_model=RawBlockchainConfig,
        )

    async def get_block_transactions(
        self,
        block_id: str,
    ) -> Transactions:
        """Get transactions from block.

        :param block_id: Block ID.
        :return: Transactions
        """
        path = f"/v2/blockchain/blocks/{block_id}/transactions"
        return await self._request(
            method="GET",
            path=path,
            response_model=Transactions,
        )

    async def get_transaction(
        self,
        transaction_id: str,
    ) -> Transaction:
        """Get transaction data.

        :param transaction_id: Transaction ID.
        :return: Transaction
        """
        path = f"/v2/blockchain/transactions/{transaction_id}"
        return await self._request(
            method="GET",
            path=path,
            response_model=Transaction,
        )

    async def get_transaction_by_message_hash(
        self,
        msg_id: str,
    ) -> Transaction:
        """Get transaction data by message hash.

        :param msg_id: Message ID.
        :return: Transaction
        """
        path = f"/v2/blockchain/messages/{msg_id}/transaction"
        return await self._request(
            method="GET",
            path=path,
            response_model=Transaction,
        )

    async def get_validators(
        self,
    ) -> Validators:
        """Get blockchain validators.

        :return: Validators
        """
        path = "/v2/blockchain/validators"
        return await self._request(
            method="GET",
            path=path,
            response_model=Validators,
        )

    async def get_masterchain_head(
        self,
    ) -> BlockchainBlock:
        """Get last known masterchain block.

        :return: BlockchainBlock
        """
        path = "/v2/blockchain/masterchain-head"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainBlock,
        )

    async def get_raw_account(
        self,
        account_id: str,
    ) -> BlockchainRawAccount:
        """Get low-level information about an account taken directly from the blockchain.

        :param account_id: Account ID.
        :return: BlockchainRawAccount
        """
        path = f"/v2/blockchain/accounts/{account_id}"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainRawAccount,
        )

    async def get_raw_accounts(
        self,
        body: dict[str, t.Any],
    ) -> BlockchainRawAccounts:
        """Get low-level information about several accounts taken directly from the blockchain.

        :param body: Request body.
        :return: BlockchainRawAccounts
        """
        path = "/v2/blockchain/accounts/_bulk"
        return await self._request(
            method="POST",
            path=path,
            body=body,
            response_model=BlockchainRawAccounts,
        )

    async def get_account_transactions(
        self,
        account_id: str,
        after_lt: int | None = None,
        before_lt: int | None = None,
        limit: int = 100,
        sort_order: str = "desc",
    ) -> Transactions:
        """Get account transactions.

        :param account_id: Account ID.
        :param after_lt: Omit this parameter to get last transactions.
        :param before_lt: Omit this parameter to get last transactions.
        :param limit: Limit.
        :param sort_order: Sort order.
        :return: Transactions
        """
        path = f"/v2/blockchain/accounts/{account_id}/transactions"
        params = {
            "after_lt": after_lt,
            "before_lt": before_lt,
            "limit": limit,
            "sort_order": sort_order,
        }
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=Transactions,
        )

    async def execute_get_method(
        self,
        account_id: str,
        method_name: str,
        args: list[str] | None = None,
    ) -> MethodExecutionResult:
        """Execute get method for account.

        :param account_id: Account ID.
        :param method_name: Contract get method name.
        :param args: Args.
        :return: MethodExecutionResult
        """
        path = f"/v2/blockchain/accounts/{account_id}/methods/{method_name}"
        params = {"args": args}
        return await self._request(
            method="GET",
            path=path,
            params=params,
            response_model=MethodExecutionResult,
        )

    async def execute_get_method_with_body(
        self,
        account_id: str,
        method_name: str,
        body: dict[str, t.Any],
    ) -> MethodExecutionResult:
        """Execute get method for account.

        :param account_id: Account ID.
        :param method_name: Contract get method name.
        :param body: Request body.
        :return: MethodExecutionResult
        """
        path = f"/v2/blockchain/accounts/{account_id}/methods/{method_name}"
        return await self._request(
            method="POST",
            path=path,
            body=body,
            response_model=MethodExecutionResult,
        )

    async def send_message(
        self,
        body: dict[str, t.Any],
    ) -> None:
        """Send message to blockchain.

        :param body: Request body.
        """
        path = "/v2/blockchain/message"
        await self._request(
            method="POST",
            path=path,
            body=body,
        )

    async def get_config(
        self,
    ) -> BlockchainConfig:
        """Get blockchain config.

        :return: BlockchainConfig
        """
        path = "/v2/blockchain/config"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainConfig,
        )

    async def get_raw_blockchain_config(
        self,
    ) -> RawBlockchainConfig:
        """Get raw blockchain config.

        :return: RawBlockchainConfig
        """
        path = "/v2/blockchain/config/raw"
        return await self._request(
            method="GET",
            path=path,
            response_model=RawBlockchainConfig,
        )

    async def account_inspect(
        self,
        account_id: str,
    ) -> BlockchainAccountInspect:
        """Blockchain account inspect.

        :param account_id: Account ID.
        :return: BlockchainAccountInspect
        """
        path = f"/v2/blockchain/accounts/{account_id}/inspect"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainAccountInspect,
        )

    async def get_library_by_hash(
        self,
        hash: str,
    ) -> BlockchainLibrary:
        """Get library cell.

        :param hash: Hash in hex (without 0x) format.
        :return: BlockchainLibrary
        """
        path = f"/v2/blockchain/libraries/{hash}"
        return await self._request(
            method="GET",
            path=path,
            response_model=BlockchainLibrary,
        )

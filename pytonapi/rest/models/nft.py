# This file is auto-generated. Do not edit manually.

from __future__ import annotations

import typing as t

from pydantic import BaseModel, Field

from pytonapi.rest.models._enums import TrustType

if t.TYPE_CHECKING:
    from pytonapi.rest.models.accounts import AccountAddress, Price

NftApprovedBy = list[str]


class ImagePreview(BaseModel):
    resolution: str
    url: str


class NftCollectionMetadataStatus(BaseModel):
    url: str | None = Field(default=None)
    is_broken: bool | None = Field(default=None)
    last_refresh_try: int | None = Field(default=None)
    last_refresh_success: int | None = Field(default=None)


class NftCollection(BaseModel):
    address: str
    next_item_index: int
    raw_collection_content: str
    approved_by: NftApprovedBy
    trust: TrustType
    owner: AccountAddress | None = Field(default=None)
    metadata: dict[str, t.Any] | None = Field(default=None)
    previews: list[ImagePreview] | None = Field(default=None)
    metadata_status: NftCollectionMetadataStatus | None = Field(default=None)


class NftCollections(BaseModel):
    nft_collections: list[NftCollection]


class Sale(BaseModel):
    address: str
    market: AccountAddress
    price: Price
    owner: AccountAddress | None = Field(default=None)


class NftItem(BaseModel):
    address: str
    index: int
    verified: bool
    metadata: dict[str, t.Any]
    approved_by: NftApprovedBy
    trust: TrustType
    owner: AccountAddress | None = Field(default=None)
    collection: t.Any | None = Field(default=None)
    sale: Sale | None = Field(default=None)
    previews: list[ImagePreview] | None = Field(default=None)
    dns: str | None = Field(default=None)
    include_cnft: bool | None = Field(default=None)
    code_hash: str | None = Field(default=None)
    data_hash: str | None = Field(default=None)


class NftItems(BaseModel):
    nft_items: list[NftItem]


class NftOperation(BaseModel):
    operation: str
    utime: int
    lt: int
    transaction_hash: str
    item: NftItem
    source: AccountAddress | None = Field(default=None)
    destination: AccountAddress | None = Field(default=None)


class NftOperations(BaseModel):
    operations: list[NftOperation]
    next_from: int | None = Field(default=None)

from typing import *

from pydantic import BaseModel, Field


class SupplyOrder(BaseModel):
    """
    None model
    """

    scanPrice: Optional[float] = Field(alias="scanPrice", default=None)

    orderUid: Optional[str] = Field(alias="orderUid", default=None)

    article: Optional[str] = Field(alias="article", default=None)

    colorCode: Optional[str] = Field(alias="colorCode", default=None)

    rid: Optional[str] = Field(alias="rid", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    offices: Optional[List[str]] = Field(alias="offices", default=None)

    skus: Optional[List[str]] = Field(alias="skus", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    warehouseId: Optional[int] = Field(alias="warehouseId", default=None)

    nmId: Optional[int] = Field(alias="nmId", default=None)

    chrtId: Optional[int] = Field(alias="chrtId", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    convertedPrice: Optional[int] = Field(alias="convertedPrice", default=None)

    currencyCode: Optional[int] = Field(alias="currencyCode", default=None)

    convertedCurrencyCode: Optional[int] = Field(alias="convertedCurrencyCode", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

    isZeroOrder: Optional[Any] = Field(alias="isZeroOrder", default=None)

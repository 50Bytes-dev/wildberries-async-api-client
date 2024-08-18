from typing import *

from pydantic import BaseModel, Field


class OrderNew(BaseModel):
    """
    None model
    """

    id: Optional[int] = Field(alias="id", default=None)

    rid: Optional[str] = Field(alias="rid", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    warehouseId: Optional[int] = Field(alias="warehouseId", default=None)

    offices: Optional[List[str]] = Field(alias="offices", default=None)

    address: Optional[Dict[str, Any]] = Field(alias="address", default=None)

    requiredMeta: Optional[List[str]] = Field(alias="requiredMeta", default=None)

    user: Optional[Dict[str, Any]] = Field(alias="user", default=None)

    skus: Optional[List[str]] = Field(alias="skus", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    convertedPrice: Optional[int] = Field(alias="convertedPrice", default=None)

    currencyCode: Optional[int] = Field(alias="currencyCode", default=None)

    convertedCurrencyCode: Optional[int] = Field(alias="convertedCurrencyCode", default=None)

    orderUid: Optional[str] = Field(alias="orderUid", default=None)

    deliveryType: Optional[str] = Field(alias="deliveryType", default=None)

    nmId: Optional[int] = Field(alias="nmId", default=None)

    chrtId: Optional[int] = Field(alias="chrtId", default=None)

    article: Optional[str] = Field(alias="article", default=None)

    colorCode: Optional[str] = Field(alias="colorCode", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

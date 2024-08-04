from typing import *

from pydantic import BaseModel, Field


class StocksItem(BaseModel):
    """
    None model

    """

    lastChangeDate: Optional[str] = Field(alias="lastChangeDate", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

    supplierArticle: Optional[str] = Field(alias="supplierArticle", default=None)

    nmId: Optional[int] = Field(alias="nmId", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    inWayToClient: Optional[int] = Field(alias="inWayToClient", default=None)

    inWayFromClient: Optional[int] = Field(alias="inWayFromClient", default=None)

    quantityFull: Optional[int] = Field(alias="quantityFull", default=None)

    category: Optional[str] = Field(alias="category", default=None)

    subject: Optional[str] = Field(alias="subject", default=None)

    brand: Optional[str] = Field(alias="brand", default=None)

    techSize: Optional[str] = Field(alias="techSize", default=None)

    Price: Optional[float] = Field(alias="Price", default=None)

    Discount: Optional[float] = Field(alias="Discount", default=None)

    isSupply: Optional[bool] = Field(alias="isSupply", default=None)

    isRealization: Optional[bool] = Field(alias="isRealization", default=None)

    SCCode: Optional[str] = Field(alias="SCCode", default=None)

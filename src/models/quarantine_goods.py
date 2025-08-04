from typing import *

from pydantic import BaseModel, Field


class QuarantineGoods(BaseModel):
    """
    None model
    """

    nmID: Optional[int] = Field(alias="nmID", default=None)

    sizeID: Optional[int] = Field(alias="sizeID", default=None)

    techSizeName: Optional[str] = Field(alias="techSizeName", default=None)

    currencyIsoCode4217: Optional[str] = Field(alias="currencyIsoCode4217", default=None)

    newPrice: Optional[float] = Field(alias="newPrice", default=None)

    oldPrice: Optional[float] = Field(alias="oldPrice", default=None)

    newDiscount: Optional[int] = Field(alias="newDiscount", default=None)

    oldDiscount: Optional[int] = Field(alias="oldDiscount", default=None)

    priceDiff: Optional[float] = Field(alias="priceDiff", default=None)

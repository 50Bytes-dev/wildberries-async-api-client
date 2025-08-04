from typing import *

from pydantic import BaseModel, Field


class SizeGood(BaseModel):
    """
    None model

    Size information
    """

    nmID: Optional[int] = Field(alias="nmID", default=None)

    sizeID: Optional[int] = Field(alias="sizeID", default=None)

    vendorCode: Optional[str] = Field(alias="vendorCode", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    currencyIsoCode4217: Optional[str] = Field(alias="currencyIsoCode4217", default=None)

    discountedPrice: Optional[float] = Field(alias="discountedPrice", default=None)

    clubDiscountedPrice: Optional[float] = Field(alias="clubDiscountedPrice", default=None)

    discount: Optional[int] = Field(alias="discount", default=None)

    clubDiscount: Optional[int] = Field(alias="clubDiscount", default=None)

    techSizeName: Optional[str] = Field(alias="techSizeName", default=None)

    editableSizePrice: Optional[bool] = Field(alias="editableSizePrice", default=None)

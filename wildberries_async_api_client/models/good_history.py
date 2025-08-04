from typing import *

from pydantic import BaseModel, Field

from .good_status import GoodStatus


class GoodHistory(BaseModel):
    """
    None model
    """

    nmID: Optional[int] = Field(alias="nmID", default=None)

    vendorCode: Optional[str] = Field(alias="vendorCode", default=None)

    sizeID: Optional[int] = Field(alias="sizeID", default=None)

    techSizeName: Optional[str] = Field(alias="techSizeName", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    currencyIsoCode4217: Optional[str] = Field(alias="currencyIsoCode4217", default=None)

    discount: Optional[int] = Field(alias="discount", default=None)

    clubDiscount: Optional[int] = Field(alias="clubDiscount", default=None)

    status: Optional[GoodStatus] = Field(alias="status", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

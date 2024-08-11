from typing import *

from pydantic import BaseModel, Field

from .good_status_buffer import GoodStatusBuffer


class GoodBufferHistory(BaseModel):
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

    status: Optional[GoodStatusBuffer] = Field(alias="status", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

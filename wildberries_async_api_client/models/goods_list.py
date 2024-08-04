from typing import *

from pydantic import BaseModel, Field


class GoodsList(BaseModel):
    """
    None model
        Размеры товара

    """

    nmID: Optional[int] = Field(alias="nmID", default=None)

    vendorCode: Optional[str] = Field(alias="vendorCode", default=None)

    sizes: Optional[List[Dict[str, Any]]] = Field(alias="sizes", default=None)

    currencyIsoCode4217: Optional[str] = Field(alias="currencyIsoCode4217", default=None)

    discount: Optional[int] = Field(alias="discount", default=None)

    editableSizePrice: Optional[bool] = Field(alias="editableSizePrice", default=None)

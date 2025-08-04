from typing import *

from pydantic import BaseModel, Field


class PromotionsGoodsList(BaseModel):
    """
    None model
    """

    id: Optional[int] = Field(alias="id", default=None)

    inAction: Optional[bool] = Field(alias="inAction", default=None)

    price: Optional[float] = Field(alias="price", default=None)

    currencyCode: Optional[str] = Field(alias="currencyCode", default=None)

    planPrice: Optional[float] = Field(alias="planPrice", default=None)

    discount: Optional[int] = Field(alias="discount", default=None)

    planDiscount: Optional[int] = Field(alias="planDiscount", default=None)

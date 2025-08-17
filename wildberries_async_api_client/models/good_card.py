from typing import *

from pydantic import BaseModel, Field


class GoodCard(BaseModel):
    """
    None model

    Order information
    """

    date: Optional[str] = Field(alias="date", default=None)

    needRefund: Optional[bool] = Field(alias="needRefund", default=None)

    nmID: Optional[int] = Field(alias="nmID", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    priceCurrency: Optional[str] = Field(alias="priceCurrency", default=None)

    rid: Optional[Union[str, int]] = Field(alias="rid", default=None)

    size: Optional[str] = Field(alias="size", default=None)

    statusID: Optional[int] = Field(alias="statusID", default=None)

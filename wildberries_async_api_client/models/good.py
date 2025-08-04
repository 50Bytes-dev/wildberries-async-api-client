from typing import *

from pydantic import BaseModel, Field


class Good(BaseModel):
    """
    None model
    """

    nmID: int = Field(alias="nmID")

    price: Optional[int] = Field(alias="price", default=None)

    discount: Optional[int] = Field(alias="discount", default=None)

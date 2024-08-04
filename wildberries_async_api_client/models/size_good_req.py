from typing import *

from pydantic import BaseModel, Field


class SizeGoodReq(BaseModel):
    """
    None model

    """

    nmID: int = Field(alias="nmID")

    sizeID: int = Field(alias="sizeID")

    price: int = Field(alias="price")

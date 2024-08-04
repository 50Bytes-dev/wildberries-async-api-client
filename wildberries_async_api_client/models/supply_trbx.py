from typing import *

from pydantic import BaseModel, Field


class SupplyTrbx(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    orders: Optional[List[int]] = Field(alias="orders", default=None)

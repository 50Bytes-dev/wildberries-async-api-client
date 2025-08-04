from typing import *

from pydantic import BaseModel, Field


class OrdersRequestAPI(BaseModel):
    """
    None model
    """

    orders: Optional[List[int]] = Field(alias="orders", default=None)

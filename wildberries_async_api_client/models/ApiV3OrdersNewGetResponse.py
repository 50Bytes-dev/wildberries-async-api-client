from typing import *

from pydantic import BaseModel, Field

from .OrderNew import OrderNew


class ApiV3OrdersNewGetResponse(BaseModel):
    """
    None model

    """

    orders: Optional[List[Optional[OrderNew]]] = Field(alias="orders", default=None)

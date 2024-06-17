from typing import *

from pydantic import BaseModel, Field

from .OrderNew import OrderNew


class NewOrdersGetResponse(BaseModel):
    """
    Model for List of new orders

    """

    orders: Optional[List[Optional[OrderNew]]] = Field(alias="orders", default=None)

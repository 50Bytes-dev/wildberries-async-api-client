from typing import *

from pydantic import BaseModel, Field

from .next import Next
from .order import Order


class ApiV3OrdersGetResponse(BaseModel):
    """
    None model
    """

    next: Optional[Next] = Field(alias="next", default=None)

    orders: Optional[List[Optional[Order]]] = Field(alias="orders", default=None)

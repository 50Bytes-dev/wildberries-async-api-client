from typing import *

from pydantic import BaseModel, Field

from .next import Next
from .order import Order


class ApiV3OrdersGetResponse(BaseModel):
    """
    None model

    """

    next: Optional[int] = Field(alias="next", default=None) # TODO correct async generator to fix model ApiV3OrdersGetResponse

    orders: Optional[List[Optional[Order]]] = Field(alias="orders", default=None)

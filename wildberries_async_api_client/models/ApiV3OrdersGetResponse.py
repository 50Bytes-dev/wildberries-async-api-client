from typing import *

from pydantic import BaseModel, Field

from .Next import Next
from .Order import Order


class ApiV3OrdersGetResponse(BaseModel):
    """
    None model

    """

    next: Optional[Next] = Field(alias="next", default=None)

    orders: Optional[List[Optional[Order]]] = Field(alias="orders", default=None)

from typing import *

from pydantic import BaseModel, Field


class ApiV3OrdersStatusPostResponse(BaseModel):
    """
    None model
    """

    orders: Optional[List[Dict[str, Any]]] = Field(alias="orders", default=None)

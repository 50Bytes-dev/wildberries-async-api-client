from typing import *

from pydantic import BaseModel, Field


class ApiV3SuppliesOrdersReshipmentGetResponse(BaseModel):
    """
    None model

    """

    orders: Optional[List[Dict[str, Any]]] = Field(alias="orders", default=None)

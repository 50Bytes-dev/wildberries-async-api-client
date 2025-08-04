from typing import *

from pydantic import BaseModel, Field


class ApiV3StocksWarehouseIdPostResponse(BaseModel):
    """
    None model
    """

    stocks: Optional[List[Dict[str, Any]]] = Field(alias="stocks", default=None)

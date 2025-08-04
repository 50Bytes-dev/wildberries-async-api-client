from typing import *

from pydantic import BaseModel, Field


class ResponsePromotionsGoodsLists(BaseModel):
    """
    None model
    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

from typing import *

from pydantic import BaseModel, Field


class AdvV1SeacatStatGetResponse(BaseModel):
    """
    None model

    """

    totalViews: Optional[int] = Field(alias="totalViews", default=None)

    totalClicks: Optional[int] = Field(alias="totalClicks", default=None)

    totalOrders: Optional[int] = Field(alias="totalOrders", default=None)

    totalSum: Optional[int] = Field(alias="totalSum", default=None)

    dates: Optional[List[Dict[str, Any]]] = Field(alias="dates", default=None)

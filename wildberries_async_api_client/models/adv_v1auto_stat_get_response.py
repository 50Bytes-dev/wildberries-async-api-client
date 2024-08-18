from typing import *

from pydantic import BaseModel, Field


class AdvV1AutoStatGetResponse(BaseModel):
    """
    None model
    """

    views: Optional[int] = Field(alias="views", default=None)

    clicks: Optional[float] = Field(alias="clicks", default=None)

    ctr: Optional[float] = Field(alias="ctr", default=None)

    cpc: Optional[float] = Field(alias="cpc", default=None)

    spend: Optional[int] = Field(alias="spend", default=None)

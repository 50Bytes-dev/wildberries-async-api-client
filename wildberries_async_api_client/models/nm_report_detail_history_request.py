from typing import *

from pydantic import BaseModel, Field


class NmReportDetailHistoryRequest(BaseModel):
    """
    None model
    """

    nmIDs: List[int] = Field(alias="nmIDs")

    period: Dict[str, Any] = Field(alias="period")

    timezone: Optional[str] = Field(alias="timezone", default=None)

    aggregationLevel: Optional[str] = Field(alias="aggregationLevel", default=None)

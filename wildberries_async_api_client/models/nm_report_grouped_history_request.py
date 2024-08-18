from typing import *

from pydantic import BaseModel, Field


class NmReportGroupedHistoryRequest(BaseModel):
    """
    None model
    """

    objectIDs: Optional[List[int]] = Field(alias="objectIDs", default=None)

    brandNames: Optional[List[str]] = Field(alias="brandNames", default=None)

    tagIDs: Optional[List[int]] = Field(alias="tagIDs", default=None)

    period: Dict[str, Any] = Field(alias="period")

    timezone: Optional[str] = Field(alias="timezone", default=None)

    aggregationLevel: Optional[str] = Field(alias="aggregationLevel", default=None)

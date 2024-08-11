from typing import *

from pydantic import BaseModel, Field


class NmReportGroupedRequest(BaseModel):
    """
    None model

    """

    objectIDs: Optional[List[int]] = Field(alias="objectIDs", default=None)

    brandNames: Optional[List[str]] = Field(alias="brandNames", default=None)

    tagIDs: Optional[List[int]] = Field(alias="tagIDs", default=None)

    timezone: Optional[str] = Field(alias="timezone", default=None)

    period: Dict[str, Any] = Field(alias="period")

    orderBy: Optional[Dict[str, Any]] = Field(alias="orderBy", default=None)

    page: int = Field(alias="page")

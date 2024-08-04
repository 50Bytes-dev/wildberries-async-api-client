from typing import *

from pydantic import BaseModel, Field


class GroupedByObjectsBrandsAndTagsReq(BaseModel):
    """
    None model

    """

    id: str = Field(alias="id")

    reportType: str = Field(alias="reportType")

    userReportName: Optional[str] = Field(alias="userReportName", default=None)

    params: Optional[Dict[str, Any]] = Field(alias="params", default=None)

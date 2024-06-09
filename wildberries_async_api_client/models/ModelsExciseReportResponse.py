from typing import *

from pydantic import BaseModel, Field

from .ModelsExciseReportResponseData import ModelsExciseReportResponseData


class ModelsExciseReportResponse(BaseModel):
    """
    None model

    """

    data: Optional[ModelsExciseReportResponseData] = Field(alias="data", default=None)

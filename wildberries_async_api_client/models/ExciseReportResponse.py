from typing import *

from pydantic import BaseModel, Field

from .ModelsExciseReportResponse import ModelsExciseReportResponse


class ExciseReportResponse(BaseModel):
    """
    None model

    """

    response: Optional[ModelsExciseReportResponse] = Field(alias="response", default=None)

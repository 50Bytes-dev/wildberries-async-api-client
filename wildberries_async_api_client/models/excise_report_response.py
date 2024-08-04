from typing import *

from pydantic import BaseModel, Field

from .models_excise_report_response import ModelsExciseReportResponse


class ExciseReportResponse(BaseModel):
    """
    None model

    """

    response: Optional[ModelsExciseReportResponse] = Field(alias="response", default=None)

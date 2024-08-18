from typing import *

from pydantic import BaseModel, Field

from .models_excise_report_response_data import ModelsExciseReportResponseData


class ModelsExciseReportResponse(BaseModel):
    """
    None model
    """

    data: Optional[ModelsExciseReportResponseData] = Field(alias="data", default=None)

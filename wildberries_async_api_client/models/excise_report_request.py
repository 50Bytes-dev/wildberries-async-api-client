from typing import *

from pydantic import BaseModel, Field


class ExciseReportRequest(BaseModel):
    """
    None model

    """

    countries: Optional[List[str]] = Field(alias="countries", default=None)

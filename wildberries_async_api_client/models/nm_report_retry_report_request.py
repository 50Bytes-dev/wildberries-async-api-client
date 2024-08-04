from typing import *

from pydantic import BaseModel, Field


class NmReportRetryReportRequest(BaseModel):
    """
    None model

    """

    downloadId: Optional[str] = Field(alias="downloadId", default=None)

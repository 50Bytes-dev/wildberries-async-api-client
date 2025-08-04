from typing import *

from pydantic import BaseModel, Field


class Response401(BaseModel):
    """
    None model
    """

    title: Optional[str] = Field(alias="title", default=None)

    detail: Optional[str] = Field(alias="detail", default=None)

    code: Optional[str] = Field(alias="code", default=None)

    requestId: Optional[str] = Field(alias="requestId", default=None)

    origin: Optional[str] = Field(alias="origin", default=None)

    status: Optional[float] = Field(alias="status", default=None)

    statusText: Optional[str] = Field(alias="statusText", default=None)

    timestamp: Optional[str] = Field(alias="timestamp", default=None)

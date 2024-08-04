from typing import *

from pydantic import BaseModel, Field


class Error400getClaims(BaseModel):
    """
    None model

    """

    title: Optional[str] = Field(alias="title", default=None)

    detail: Optional[str] = Field(alias="detail", default=None)

    requestId: Optional[str] = Field(alias="requestId", default=None)

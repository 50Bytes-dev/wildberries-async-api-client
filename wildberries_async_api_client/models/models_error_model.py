from typing import *

from pydantic import BaseModel, Field


class ModelsErrorModel(BaseModel):
    """
    None model

    """

    status: Optional[int] = Field(alias="status", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    detail: Optional[str] = Field(alias="detail", default=None)

    requestID: Optional[str] = Field(alias="requestID", default=None)

    origin: Optional[str] = Field(alias="origin", default=None)

from typing import *

from pydantic import BaseModel, Field


class File(BaseModel):
    """
    None model

    """

    contentType: Optional[str] = Field(alias="contentType", default=None)

    date: Optional[str] = Field(alias="date", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    url: Optional[str] = Field(alias="url", default=None)

    size: Optional[int] = Field(alias="size", default=None)

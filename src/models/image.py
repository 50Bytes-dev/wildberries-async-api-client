from typing import *

from pydantic import BaseModel, Field


class Image(BaseModel):
    """
    None model

    Image
    """

    date: Optional[str] = Field(alias="date", default=None)

    downloadID: Optional[str] = Field(alias="downloadID", default=None)

    url: Optional[str] = Field(alias="url", default=None)

from typing import *

from pydantic import BaseModel, Field


class Image(BaseModel):
    """
    None model
        Изображение

    """

    date: Optional[str] = Field(alias="date", default=None)

    url: Optional[str] = Field(alias="url", default=None)

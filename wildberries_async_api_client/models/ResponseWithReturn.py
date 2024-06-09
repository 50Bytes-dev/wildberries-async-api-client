from typing import *

from pydantic import BaseModel, Field


class ResponseWithReturn(BaseModel):
    """
    None model

    """

    total: Optional[int] = Field(alias="total", default=None)

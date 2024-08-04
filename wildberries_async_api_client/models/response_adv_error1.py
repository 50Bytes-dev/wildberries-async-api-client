from typing import *

from pydantic import BaseModel, Field


class ResponseAdvError1(BaseModel):
    """
    None model

    """

    error: Optional[str] = Field(alias="error", default=None)

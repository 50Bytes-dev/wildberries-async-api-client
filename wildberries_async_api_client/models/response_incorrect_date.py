from typing import *

from pydantic import BaseModel, Field


class ResponseIncorrectDate(BaseModel):
    """
    None model

    """

    error: Optional[str] = Field(alias="error", default=None)

from typing import *

from pydantic import BaseModel, Field


class ErrorFailedParseData(BaseModel):
    """
    None model
    """

    errorText: Optional[str] = Field(alias="errorText", default=None)

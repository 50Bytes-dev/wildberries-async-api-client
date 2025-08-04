from typing import *

from pydantic import BaseModel, Field


class ErrorWrongParameters(BaseModel):
    """
    None model
    """

    errorText: Optional[str] = Field(alias="errorText", default=None)

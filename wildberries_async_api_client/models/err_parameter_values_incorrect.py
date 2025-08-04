from typing import *

from pydantic import BaseModel, Field


class ErrParameterValuesIncorrect(BaseModel):
    """
    None model
    """

    errorText: Optional[str] = Field(alias="errorText", default=None)

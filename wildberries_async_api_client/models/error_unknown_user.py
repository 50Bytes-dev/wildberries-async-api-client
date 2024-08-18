from typing import *

from pydantic import BaseModel, Field


class ErrorUnknownUser(BaseModel):
    """
    None model
    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

    error: Optional[bool] = Field(alias="error", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

    code: Optional[int] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

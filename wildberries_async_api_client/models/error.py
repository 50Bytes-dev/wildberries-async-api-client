from typing import *

from pydantic import BaseModel, Field


class Error(BaseModel):
    """
    None model

    """

    code: Optional[str] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

    error: Optional[str] = Field(alias="error", default=None)

from typing import *

from pydantic import BaseModel, Field


class StatusNotAcceptable(BaseModel):
    """
    None model
    """

    code: Optional[str] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

from typing import *

from pydantic import BaseModel, Field


class Response401(BaseModel):
    """
    None model
    """

    code: Optional[int] = Field(alias="code", default=None)

    message: Optional[str] = Field(alias="message", default=None)

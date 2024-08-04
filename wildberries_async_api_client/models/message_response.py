from typing import *

from pydantic import BaseModel, Field


class MessageResponse(BaseModel):
    """
    None model

    """

    errors: Optional[List[str]] = Field(alias="errors", default=None)

    result: Optional[Dict[str, Any]] = Field(alias="result", default=None)

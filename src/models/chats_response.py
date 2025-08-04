from typing import *

from pydantic import BaseModel, Field

from .chat import Chat


class ChatsResponse(BaseModel):
    """
    None model
    """

    result: Optional[List[Optional[Chat]]] = Field(alias="result", default=None)

    errors: Optional[List[str]] = Field(alias="errors", default=None)

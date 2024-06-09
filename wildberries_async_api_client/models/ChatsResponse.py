from typing import *

from pydantic import BaseModel, Field

from .Chat import Chat


class ChatsResponse(BaseModel):
    """
    None model

    """

    result: Optional[List[Optional[Chat]]] = Field(alias="result", default=None)

    errors: Optional[Any] = Field(alias="errors", default=None)

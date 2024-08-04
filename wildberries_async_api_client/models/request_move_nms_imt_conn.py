from typing import *

from pydantic import BaseModel, Field


class RequestMoveNmsImtConn(BaseModel):
    """
    None model

    """

    targetIMT: int = Field(alias="targetIMT")

    nmIDs: List[int] = Field(alias="nmIDs")

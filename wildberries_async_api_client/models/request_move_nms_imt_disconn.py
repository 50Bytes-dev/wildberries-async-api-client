from typing import *

from pydantic import BaseModel, Field


class RequestMoveNmsImtDisconn(BaseModel):
    """
    None model
    """

    nmIDs: List[int] = Field(alias="nmIDs")

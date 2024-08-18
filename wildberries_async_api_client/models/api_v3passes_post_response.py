from typing import *

from pydantic import BaseModel, Field


class ApiV3PassesPostResponse(BaseModel):
    """
    None model
    """

    id: Optional[int] = Field(alias="id", default=None)

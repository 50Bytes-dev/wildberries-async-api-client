from typing import *

from pydantic import BaseModel, Field


class ApiV3WarehousesPostResponse(BaseModel):
    """
    None model
    """

    id: Optional[int] = Field(alias="id", default=None)

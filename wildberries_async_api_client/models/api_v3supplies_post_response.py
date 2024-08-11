from typing import *

from pydantic import BaseModel, Field


class ApiV3SuppliesPostResponse(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

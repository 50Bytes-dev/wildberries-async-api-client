from typing import *

from pydantic import BaseModel, Field


class NewSuppliesPostResponse(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

from typing import *

from pydantic import BaseModel, Field


class V0getConfigCategoriesResponse(BaseModel):
    """
    None model
    """

    id: int = Field(alias="id")

    name: str = Field(alias="name")

    cpm_min: int = Field(alias="cpm_min")

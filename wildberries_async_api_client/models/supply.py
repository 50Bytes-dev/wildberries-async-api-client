from typing import *

from pydantic import BaseModel, Field


class Supply(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    done: Optional[bool] = Field(alias="done", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    closedAt: Optional[str] = Field(alias="closedAt", default=None)

    scanDt: Optional[str] = Field(alias="scanDt", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

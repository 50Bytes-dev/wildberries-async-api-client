from typing import *

from pydantic import BaseModel, Field


class V0advertMultiBidItem(BaseModel):
    """
    None model
    """

    nm: int = Field(alias="nm")

    bid: int = Field(alias="bid")

from typing import *

from pydantic import BaseModel, Field


class ClubDiscReq(BaseModel):
    """
    None model
    """

    nmID: int = Field(alias="nmID")

    clubDiscount: int = Field(alias="clubDiscount")

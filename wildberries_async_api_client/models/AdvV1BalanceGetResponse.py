from typing import *

from pydantic import BaseModel, Field


class AdvV1BalanceGetResponse(BaseModel):
    """
    None model

    """

    balance: Optional[int] = Field(alias="balance", default=None)

    net: Optional[int] = Field(alias="net", default=None)

    bonus: Optional[int] = Field(alias="bonus", default=None)

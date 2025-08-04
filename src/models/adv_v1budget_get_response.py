from typing import *

from pydantic import BaseModel, Field


class AdvV1BudgetGetResponse(BaseModel):
    """
    None model
    """

    cash: Optional[int] = Field(alias="cash", default=None)

    netting: Optional[int] = Field(alias="netting", default=None)

    total: Optional[int] = Field(alias="total", default=None)

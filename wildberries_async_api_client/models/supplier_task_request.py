from typing import *

from pydantic import BaseModel, Field

from .goods import Goods


class SupplierTaskRequest(BaseModel):
    """
    None model

    """

    data: Optional[Goods] = Field(alias="data", default=None)

from typing import *

from pydantic import BaseModel, Field

from .SizeGoodsBody import SizeGoodsBody


class SupplierTaskRequestSize(BaseModel):
    """
    None model

    """

    data: Optional[SizeGoodsBody] = Field(alias="data", default=None)

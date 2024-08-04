from typing import *

from pydantic import BaseModel, Field

from .size_goods_body import SizeGoodsBody


class SupplierTaskRequestSize(BaseModel):
    """
    None model

    """

    data: Optional[SizeGoodsBody] = Field(alias="data", default=None)

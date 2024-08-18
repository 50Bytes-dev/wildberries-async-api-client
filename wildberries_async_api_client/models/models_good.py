from typing import *

from pydantic import BaseModel, Field


class ModelsGood(BaseModel):
    """
    None model
    """

    quantity: Optional[int] = Field(alias="quantity", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

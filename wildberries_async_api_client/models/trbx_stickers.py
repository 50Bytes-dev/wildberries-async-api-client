from typing import *

from pydantic import BaseModel, Field


class TrbxStickers(BaseModel):
    """
    None model
    """

    barcode: Optional[str] = Field(alias="barcode", default=None)

    file: Optional[str] = Field(alias="file", default=None)

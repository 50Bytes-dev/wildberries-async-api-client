from typing import *

from pydantic import BaseModel, Field

from .TrbxStickers import TrbxStickers


class ApiV3SuppliesSupplyIdTrbxStickersPostResponse(BaseModel):
    """
    None model

    """

    stickers: Optional[List[Optional[TrbxStickers]]] = Field(alias="stickers", default=None)

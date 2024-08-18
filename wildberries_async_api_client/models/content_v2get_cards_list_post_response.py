from typing import *

from pydantic import BaseModel, Field


class ContentV2GetCardsListPostResponse(BaseModel):
    """
    None model
    """

    cards: Optional[List[Dict[str, Any]]] = Field(alias="cards", default=None)

    cursor: Optional[Dict[str, Any]] = Field(alias="cursor", default=None)

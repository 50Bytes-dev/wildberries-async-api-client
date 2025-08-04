from typing import *

from pydantic import BaseModel, Field


class AdvV1PromotionCountGetResponse(BaseModel):
    """
    None model
    """

    adverts: Optional[List[Dict[str, Any]]] = Field(alias="adverts", default=None)

    all: Optional[int] = Field(alias="all", default=None)

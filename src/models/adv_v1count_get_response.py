from typing import *

from pydantic import BaseModel, Field


class AdvV1CountGetResponse(BaseModel):
    """
    None model
    """

    all: Optional[int] = Field(alias="all", default=None)

    adverts: Optional[Dict[str, Any]] = Field(alias="adverts", default=None)

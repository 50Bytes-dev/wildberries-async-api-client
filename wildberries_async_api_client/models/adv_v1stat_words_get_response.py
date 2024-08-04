from typing import *

from pydantic import BaseModel, Field


class AdvV1StatWordsGetResponse(BaseModel):
    """
    None model

    """

    words: Optional[Dict[str, Any]] = Field(alias="words", default=None)

    stat: Optional[List[Dict[str, Any]]] = Field(alias="stat", default=None)

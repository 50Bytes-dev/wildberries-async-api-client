from typing import *

from pydantic import BaseModel, Field


class AdvV2AutoStatWordsGetResponse(BaseModel):
    """
    None model
    """

    excluded: Optional[List[str]] = Field(alias="excluded", default=None)

    clusters: Optional[List[Dict[str, Any]]] = Field(alias="clusters", default=None)

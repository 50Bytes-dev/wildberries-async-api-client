from typing import *

from pydantic import BaseModel, Field


class AdvV2AutoDailyWordsGetResponse(BaseModel):
    """
    None model
    """

    date: Optional[str] = Field(alias="date", default=None)

    stat: Optional[List[Dict[str, Any]]] = Field(alias="stat", default=None)

from typing import *

from pydantic import BaseModel, Field


class ResponseGoodHistories(BaseModel):
    """
    None model
    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

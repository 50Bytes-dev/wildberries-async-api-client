from typing import *

from pydantic import BaseModel, Field


class ResponseErrorStatistics(BaseModel):
    """
    None model

    """

    errors: Optional[List[str]] = Field(alias="errors", default=None)

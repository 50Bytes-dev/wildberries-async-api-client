from typing import *

from pydantic import BaseModel, Field


class ApiV3SuppliesSupplyIdTrbxPostResponse(BaseModel):
    """
    None model
    """

    trbxIds: Optional[List[str]] = Field(alias="trbxIds", default=None)

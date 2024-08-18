from typing import *

from pydantic import BaseModel, Field


class GetClaimsSuccessResponse(BaseModel):
    """
    None model
    """

    claims: Optional[List[Dict[str, Any]]] = Field(alias="claims", default=None)

    total: Optional[int] = Field(alias="total", default=None)

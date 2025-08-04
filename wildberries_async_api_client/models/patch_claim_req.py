from typing import *

from pydantic import BaseModel, Field


class PatchClaimReq(BaseModel):
    """
    None model
    """

    id: str = Field(alias="id")

    action: str = Field(alias="action")

    comment: Optional[str] = Field(alias="comment", default=None)

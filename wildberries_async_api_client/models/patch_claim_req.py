from typing import *

from pydantic import BaseModel, Field


class PatchClaimReq(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    action: Optional[str] = Field(alias="action", default=None)

from typing import *

from pydantic import BaseModel, Field

from .SupplyTrbx import SupplyTrbx


class ApiV3SuppliesSupplyIdTrbxGetResponse(BaseModel):
    """
    None model

    """

    trbxes: Optional[List[Optional[SupplyTrbx]]] = Field(alias="trbxes", default=None)

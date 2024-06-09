from typing import *

from pydantic import BaseModel, Field

from .ModelsReturnTariffsResponse import ModelsReturnTariffsResponse


class ReturnTariffsResponse(BaseModel):
    """
    None model

    """

    response: Optional[ModelsReturnTariffsResponse] = Field(alias="response", default=None)

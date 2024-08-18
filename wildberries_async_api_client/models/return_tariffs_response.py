from typing import *

from pydantic import BaseModel, Field

from .models_return_tariffs_response import ModelsReturnTariffsResponse


class ReturnTariffsResponse(BaseModel):
    """
    None model
    """

    response: Optional[ModelsReturnTariffsResponse] = Field(alias="response", default=None)

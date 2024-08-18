from typing import *

from pydantic import BaseModel, Field

from .models_tariffs_box_response import ModelsTariffsBoxResponse


class TariffsBoxResponse(BaseModel):
    """
    None model
    """

    response: Optional[ModelsTariffsBoxResponse] = Field(alias="response", default=None)

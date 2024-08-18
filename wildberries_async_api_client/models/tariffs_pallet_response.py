from typing import *

from pydantic import BaseModel, Field

from .models_tariffs_pallet_response import ModelsTariffsPalletResponse


class TariffsPalletResponse(BaseModel):
    """
    None model
    """

    response: Optional[ModelsTariffsPalletResponse] = Field(alias="response", default=None)

from typing import *

from pydantic import BaseModel, Field

from .ModelsTariffsPalletResponse import ModelsTariffsPalletResponse


class TariffsPalletResponse(BaseModel):
    """
    None model

    """

    response: Optional[ModelsTariffsPalletResponse] = Field(alias="response", default=None)

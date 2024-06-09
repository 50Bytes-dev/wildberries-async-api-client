from typing import *

from pydantic import BaseModel, Field

from .ModelsWarehousesPalletRates import ModelsWarehousesPalletRates


class ModelsTariffsPalletResponse(BaseModel):
    """
    None model

    """

    data: Optional[ModelsWarehousesPalletRates] = Field(alias="data", default=None)

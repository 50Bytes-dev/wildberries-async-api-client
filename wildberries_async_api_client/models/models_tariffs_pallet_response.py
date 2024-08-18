from typing import *

from pydantic import BaseModel, Field

from .models_warehouses_pallet_rates import ModelsWarehousesPalletRates


class ModelsTariffsPalletResponse(BaseModel):
    """
    None model
    """

    data: Optional[ModelsWarehousesPalletRates] = Field(alias="data", default=None)

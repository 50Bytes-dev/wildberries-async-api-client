from typing import *

from pydantic import BaseModel, Field

from .models_warehouses_return_rates import ModelsWarehousesReturnRates


class ModelsReturnTariffsResponse(BaseModel):
    """
    None model

    """

    data: Optional[ModelsWarehousesReturnRates] = Field(alias="data", default=None)

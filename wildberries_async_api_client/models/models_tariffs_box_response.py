from typing import *

from pydantic import BaseModel, Field

from .models_warehouses_box_rates import ModelsWarehousesBoxRates


class ModelsTariffsBoxResponse(BaseModel):
    """
    None model
    """

    data: Optional[ModelsWarehousesBoxRates] = Field(alias="data", default=None)

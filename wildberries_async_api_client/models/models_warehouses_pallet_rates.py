from typing import *

from pydantic import BaseModel, Field

from .models_warehouse_pallet_rates import ModelsWarehousePalletRates


class ModelsWarehousesPalletRates(BaseModel):
    """
    None model

    """

    dtFromMin: Optional[str] = Field(alias="dtFromMin", default=None)

    dtNextPallet: Optional[str] = Field(alias="dtNextPallet", default=None)

    dtTillMax: Optional[str] = Field(alias="dtTillMax", default=None)

    warehouseList: Optional[List[Optional[ModelsWarehousePalletRates]]] = Field(alias="warehouseList", default=None)

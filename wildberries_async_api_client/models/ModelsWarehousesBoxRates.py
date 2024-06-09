from typing import *

from pydantic import BaseModel, Field

from .ModelsWarehouseBoxRates import ModelsWarehouseBoxRates


class ModelsWarehousesBoxRates(BaseModel):
    """
    None model

    """

    dtFromMin: Optional[str] = Field(alias="dtFromMin", default=None)

    dtNextBox: Optional[str] = Field(alias="dtNextBox", default=None)

    dtTillMax: Optional[str] = Field(alias="dtTillMax", default=None)

    warehouseList: Optional[List[Optional[ModelsWarehouseBoxRates]]] = Field(alias="warehouseList", default=None)

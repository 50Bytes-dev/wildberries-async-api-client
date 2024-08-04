from typing import *

from pydantic import BaseModel, Field

from .models_warehouse_return_rates import ModelsWarehouseReturnRates


class ModelsWarehousesReturnRates(BaseModel):
    """
    None model

    """

    dtNextDeliveryDumpKgt: Optional[str] = Field(alias="dtNextDeliveryDumpKgt", default=None)

    dtNextDeliveryDumpSrg: Optional[str] = Field(alias="dtNextDeliveryDumpSrg", default=None)

    dtNextDeliveryDumpSup: Optional[str] = Field(alias="dtNextDeliveryDumpSup", default=None)

    warehouseList: Optional[List[Optional[ModelsWarehouseReturnRates]]] = Field(alias="warehouseList", default=None)

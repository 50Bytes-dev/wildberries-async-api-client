from typing import *

from pydantic import BaseModel, Field


class ModelsWarehouseBoxRates(BaseModel):
    """
    None model

    """

    boxDeliveryAndStorageExpr: Optional[str] = Field(alias="boxDeliveryAndStorageExpr", default=None)

    boxDeliveryBase: Optional[str] = Field(alias="boxDeliveryBase", default=None)

    boxDeliveryLiter: Optional[str] = Field(alias="boxDeliveryLiter", default=None)

    boxStorageBase: Optional[str] = Field(alias="boxStorageBase", default=None)

    boxStorageLiter: Optional[str] = Field(alias="boxStorageLiter", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

from typing import *

from pydantic import BaseModel, Field


class ModelsWarehousePalletRates(BaseModel):
    """
    None model

    """

    palletDeliveryExpr: Optional[str] = Field(alias="palletDeliveryExpr", default=None)

    palletDeliveryValueBase: Optional[str] = Field(alias="palletDeliveryValueBase", default=None)

    palletDeliveryValueLiter: Optional[str] = Field(alias="palletDeliveryValueLiter", default=None)

    palletStorageExpr: Optional[str] = Field(alias="palletStorageExpr", default=None)

    palletStorageValueExpr: Optional[str] = Field(alias="palletStorageValueExpr", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

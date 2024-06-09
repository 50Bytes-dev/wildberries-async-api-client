from typing import *

from pydantic import BaseModel, Field

from .ModelsWarehousesReturnRates import ModelsWarehousesReturnRates


class ModelsReturnTariffsResponse(BaseModel):
    """
    None model

    """

    data: Optional[ModelsWarehousesReturnRates] = Field(alias="data", default=None)

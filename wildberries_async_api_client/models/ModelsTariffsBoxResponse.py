from typing import *

from pydantic import BaseModel, Field

from .ModelsWarehousesBoxRates import ModelsWarehousesBoxRates


class ModelsTariffsBoxResponse(BaseModel):
    """
    None model

    """

    data: Optional[ModelsWarehousesBoxRates] = Field(alias="data", default=None)

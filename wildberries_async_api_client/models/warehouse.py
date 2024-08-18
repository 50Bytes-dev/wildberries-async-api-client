from typing import *

from pydantic import BaseModel, Field


class Warehouse(BaseModel):
    """
    None model

    Данные о складе продавца
    """

    name: Optional[str] = Field(alias="name", default=None)

    officeId: Optional[int] = Field(alias="officeId", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

    deliveryType: Optional[int] = Field(alias="deliveryType", default=None)

from typing import *

from pydantic import BaseModel, Field


class ModelsWarehousesResultItems(BaseModel):
    """
    None model
    """

    ID: Optional[int] = Field(alias="ID", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    address: Optional[str] = Field(alias="address", default=None)

    workTime: Optional[str] = Field(alias="workTime", default=None)

    acceptsQr: Optional[bool] = Field(alias="acceptsQr", default=None)

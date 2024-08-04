from typing import *

from pydantic import BaseModel, Field


class ModelsAcceptanceCoefficient(BaseModel):
    """
    None model

    """

    date: Optional[str] = Field(alias="date", default=None)

    coefficient: Optional[float] = Field(alias="coefficient", default=None)

    warehouseID: Optional[int] = Field(alias="warehouseID", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

    boxTypeName: Optional[str] = Field(alias="boxTypeName", default=None)

    boxTypeID: Optional[int] = Field(alias="boxTypeID", default=None)

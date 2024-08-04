from typing import *

from pydantic import BaseModel, Field


class ModelsWarehouseReturnRates(BaseModel):
    """
    None model

    """

    deliveryDumpKgtOfficeBase: Optional[str] = Field(alias="deliveryDumpKgtOfficeBase", default=None)

    deliveryDumpKgtOfficeLiter: Optional[str] = Field(alias="deliveryDumpKgtOfficeLiter", default=None)

    deliveryDumpKgtReturnExpr: Optional[str] = Field(alias="deliveryDumpKgtReturnExpr", default=None)

    deliveryDumpSrgOfficeExpr: Optional[str] = Field(alias="deliveryDumpSrgOfficeExpr", default=None)

    deliveryDumpSrgReturnExpr: Optional[str] = Field(alias="deliveryDumpSrgReturnExpr", default=None)

    deliveryDumpSupCourierBase: Optional[str] = Field(alias="deliveryDumpSupCourierBase", default=None)

    deliveryDumpSupCourierLiter: Optional[str] = Field(alias="deliveryDumpSupCourierLiter", default=None)

    deliveryDumpSupOfficeBase: Optional[str] = Field(alias="deliveryDumpSupOfficeBase", default=None)

    deliveryDumpSupOfficeLiter: Optional[str] = Field(alias="deliveryDumpSupOfficeLiter", default=None)

    deliveryDumpSupReturnExpr: Optional[str] = Field(alias="deliveryDumpSupReturnExpr", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

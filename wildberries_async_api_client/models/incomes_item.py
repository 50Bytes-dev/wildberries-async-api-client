from typing import *

from pydantic import BaseModel, Field


class IncomesItem(BaseModel):
    """
    None model
    """

    incomeId: Optional[int] = Field(alias="incomeId", default=None)

    number: Optional[str] = Field(alias="number", default=None)

    date: Optional[str] = Field(alias="date", default=None)

    lastChangeDate: Optional[str] = Field(alias="lastChangeDate", default=None)

    supplierArticle: Optional[str] = Field(alias="supplierArticle", default=None)

    techSize: Optional[str] = Field(alias="techSize", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    totalPrice: Optional[float] = Field(alias="totalPrice", default=None)

    dateClose: Optional[str] = Field(alias="dateClose", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

    nmId: Optional[int] = Field(alias="nmId", default=None)

    status: Optional[str] = Field(alias="status", default=None)

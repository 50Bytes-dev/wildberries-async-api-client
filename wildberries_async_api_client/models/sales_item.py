from typing import *

from pydantic import BaseModel, Field


class SalesItem(BaseModel):
    """
    None model

    """

    date: Optional[str] = Field(alias="date", default=None)

    lastChangeDate: Optional[str] = Field(alias="lastChangeDate", default=None)

    warehouseName: Optional[str] = Field(alias="warehouseName", default=None)

    countryName: Optional[str] = Field(alias="countryName", default=None)

    oblastOkrugName: Optional[str] = Field(alias="oblastOkrugName", default=None)

    regionName: Optional[str] = Field(alias="regionName", default=None)

    supplierArticle: Optional[str] = Field(alias="supplierArticle", default=None)

    nmId: Optional[int] = Field(alias="nmId", default=None)

    barcode: Optional[str] = Field(alias="barcode", default=None)

    category: Optional[str] = Field(alias="category", default=None)

    subject: Optional[str] = Field(alias="subject", default=None)

    brand: Optional[str] = Field(alias="brand", default=None)

    techSize: Optional[str] = Field(alias="techSize", default=None)

    incomeID: Optional[int] = Field(alias="incomeID", default=None)

    isSupply: Optional[bool] = Field(alias="isSupply", default=None)

    isRealization: Optional[bool] = Field(alias="isRealization", default=None)

    totalPrice: Optional[float] = Field(alias="totalPrice", default=None)

    discountPercent: Optional[int] = Field(alias="discountPercent", default=None)

    spp: Optional[float] = Field(alias="spp", default=None)

    paymentSaleAmount: Optional[int] = Field(alias="paymentSaleAmount", default=None)

    forPay: Optional[float] = Field(alias="forPay", default=None)

    finishedPrice: Optional[float] = Field(alias="finishedPrice", default=None)

    priceWithDisc: Optional[float] = Field(alias="priceWithDisc", default=None)

    saleID: Optional[str] = Field(alias="saleID", default=None)

    orderType: Optional[str] = Field(alias="orderType", default=None)

    sticker: Optional[str] = Field(alias="sticker", default=None)

    gNumber: Optional[str] = Field(alias="gNumber", default=None)

    srid: Optional[str] = Field(alias="srid", default=None)

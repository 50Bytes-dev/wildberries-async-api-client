from typing import *

from pydantic import BaseModel, Field


class ProductRating(BaseModel):
    """
    None model
    """

    nmId: Optional[int] = Field(alias="nmId", default=None)

    imtId: Optional[int] = Field(alias="imtId", default=None)

    valuationsSum: Optional[int] = Field(alias="valuationsSum", default=None)

    feedbacksCount: Optional[int] = Field(alias="feedbacksCount", default=None)

    valuation: Optional[float] = Field(alias="valuation", default=None)

    productName: Optional[str] = Field(alias="productName", default=None)

    supplierArticle: Optional[str] = Field(alias="supplierArticle", default=None)

    brandName: Optional[str] = Field(alias="brandName", default=None)

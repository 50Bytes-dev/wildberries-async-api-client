from typing import *

from pydantic import BaseModel, Field


class Meta(BaseModel):
    """
    None model
        Метаданные заказа

    """

    imei: Optional[str] = Field(alias="imei", default=None)

    uin: Optional[str] = Field(alias="uin", default=None)

    gtin: Optional[str] = Field(alias="gtin", default=None)

    sgtin: Optional[str] = Field(alias="sgtin", default=None)

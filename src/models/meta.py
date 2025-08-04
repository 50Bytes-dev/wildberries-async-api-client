from typing import *

from pydantic import BaseModel, Field


class Meta(BaseModel):
    """
    None model

    Order metadata
    """

    imei: Optional[Dict[str, Any]] = Field(alias="imei", default=None)

    uin: Optional[Dict[str, Any]] = Field(alias="uin", default=None)

    gtin: Optional[Dict[str, Any]] = Field(alias="gtin", default=None)

    sgtin: Optional[Dict[str, Any]] = Field(alias="sgtin", default=None)

    expiration: Optional[Dict[str, Any]] = Field(alias="expiration", default=None)

from typing import *

from pydantic import BaseModel, Field


class Office(BaseModel):
    """
    None model

    Office details
    """

    address: Optional[str] = Field(alias="address", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    city: Optional[str] = Field(alias="city", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    longitude: Optional[float] = Field(alias="longitude", default=None)

    latitude: Optional[float] = Field(alias="latitude", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

    deliveryType: Optional[int] = Field(alias="deliveryType", default=None)

    federalDistrict: Optional[str] = Field(alias="federalDistrict", default=None)

    selected: Optional[bool] = Field(alias="selected", default=None)

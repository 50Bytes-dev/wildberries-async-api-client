from typing import *

from pydantic import BaseModel, Field


class CrossborderTurkeyClientInfo(BaseModel):
    """
    None model
    """

    firstName: Optional[str] = Field(alias="firstName", default=None)

    fullName: Optional[str] = Field(alias="fullName", default=None)

    lastName: Optional[str] = Field(alias="lastName", default=None)

    middleName: Optional[str] = Field(alias="middleName", default=None)

    orderID: Optional[int] = Field(alias="orderID", default=None)

    phone: Optional[str] = Field(alias="phone", default=None)

    phoneCode: Optional[str] = Field(alias="phoneCode", default=None)

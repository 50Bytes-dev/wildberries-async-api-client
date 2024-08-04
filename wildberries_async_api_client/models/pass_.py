from typing import *

from pydantic import BaseModel, Field


class Pass(BaseModel):
    """
    None model
        Данные о пропуске продавца

    """

    firstName: Optional[str] = Field(alias="firstName", default=None)

    dateEnd: Optional[str] = Field(alias="dateEnd", default=None)

    lastName: Optional[str] = Field(alias="lastName", default=None)

    carModel: Optional[str] = Field(alias="carModel", default=None)

    carNumber: Optional[str] = Field(alias="carNumber", default=None)

    officeName: Optional[str] = Field(alias="officeName", default=None)

    officeAddress: Optional[str] = Field(alias="officeAddress", default=None)

    officeId: Optional[int] = Field(alias="officeId", default=None)

    id: Optional[int] = Field(alias="id", default=None)

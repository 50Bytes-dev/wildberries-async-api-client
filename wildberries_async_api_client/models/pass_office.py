from typing import *

from pydantic import BaseModel, Field


class PassOffice(BaseModel):
    """
    None model

    Данные о складе, для которого требуется пропуск
    """

    name: Optional[str] = Field(alias="name", default=None)

    address: Optional[str] = Field(alias="address", default=None)

    id: Optional[int] = Field(alias="id", default=None)

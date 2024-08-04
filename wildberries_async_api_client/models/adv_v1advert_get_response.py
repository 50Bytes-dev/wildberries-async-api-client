from typing import *

from pydantic import BaseModel, Field


class AdvV1AdvertGetResponse(BaseModel):
    """
    None model

    """

    advertId: Optional[int] = Field(alias="advertId", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    brand: Optional[str] = Field(alias="brand", default=None)

    type: Optional[int] = Field(alias="type", default=None)

    status: Optional[int] = Field(alias="status", default=None)

    createTime: Optional[str] = Field(alias="createTime", default=None)

    extended: Optional[Dict[str, Any]] = Field(alias="extended", default=None)

    items: Optional[List[Dict[str, Any]]] = Field(alias="items", default=None)

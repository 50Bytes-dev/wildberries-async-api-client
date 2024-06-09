from typing import *

from pydantic import BaseModel, Field

from .Meta import Meta


class ApiV3OrdersOrderIdMetaGetResponse(BaseModel):
    """
    None model

    """

    meta: Optional[Meta] = Field(alias="meta", default=None)

from typing import *

from pydantic import BaseModel, Field

from .meta import Meta


class ApiV3OrdersOrderIdMetaGetResponse(BaseModel):
    """
    None model
    """

    meta: Optional[Meta] = Field(alias="meta", default=None)

from typing import *

from pydantic import BaseModel, Field

from .next import Next
from .supply import Supply


class ApiV3SuppliesGetResponse(BaseModel):
    """
    None model
    """

    next: Optional[Next] = Field(alias="next", default=None)

    supplies: Optional[List[Optional[Supply]]] = Field(alias="supplies", default=None)

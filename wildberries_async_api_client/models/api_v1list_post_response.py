from typing import *

from pydantic import BaseModel, Field


class ApiV1ListPostResponse(BaseModel):
    """
    None model

    """

    data: Optional[List[Dict[str, Any]]] = Field(alias="data", default=None)

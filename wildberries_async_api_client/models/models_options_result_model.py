from typing import *

from pydantic import BaseModel, Field


class ModelsOptionsResultModel(BaseModel):
    """
    None model

    """

    result: Optional[List[Dict[str, Any]]] = Field(alias="result", default=None)

    requestID: Optional[str] = Field(alias="requestID", default=None)

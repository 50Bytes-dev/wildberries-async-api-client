from typing import *

from pydantic import BaseModel, Field


class UploadSuccessResponse(BaseModel):
    """
    None model
    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

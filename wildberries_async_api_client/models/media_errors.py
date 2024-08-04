from typing import *

from pydantic import BaseModel, Field


class MediaErrors(BaseModel):
    """
    None model

    """

    additionalErrors: Optional[Dict[str, Any]] = Field(alias="additionalErrors", default=None)

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

    error: Optional[bool] = Field(alias="error", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

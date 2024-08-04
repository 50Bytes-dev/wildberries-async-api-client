from typing import *

from pydantic import BaseModel, Field


class ContentV2CardsRecoverPostResponse(BaseModel):
    """
    None model

    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

    error: Optional[bool] = Field(alias="error", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

    additionalErrors: Optional[Dict[str, Any]] = Field(alias="additionalErrors", default=None)

from typing import *

from pydantic import BaseModel, Field


class ApiV1QuestionsCountGetResponse(BaseModel):
    """
    None model

    """

    data: Optional[int] = Field(alias="data", default=None)

    error: Optional[bool] = Field(alias="error", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

    additionalErrors: Optional[List[str]] = Field(alias="additionalErrors", default=None)

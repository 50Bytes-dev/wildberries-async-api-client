from typing import *

from pydantic import BaseModel, Field

from .CreateTaskResponseData import CreateTaskResponseData


class CreateTaskResponse(BaseModel):
    """
    None model

    """

    data: Optional[CreateTaskResponseData] = Field(alias="data", default=None)

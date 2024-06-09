from typing import *

from pydantic import BaseModel, Field

from .GetTasksResponseData import GetTasksResponseData


class GetTasksResponse(BaseModel):
    """
    None model

    """

    data: Optional[GetTasksResponseData] = Field(alias="data", default=None)

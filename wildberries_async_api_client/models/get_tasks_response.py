from typing import *

from pydantic import BaseModel, Field

from .get_tasks_response_data import GetTasksResponseData


class GetTasksResponse(BaseModel):
    """
    None model

    """

    data: Optional[GetTasksResponseData] = Field(alias="data", default=None)

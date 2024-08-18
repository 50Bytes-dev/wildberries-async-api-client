from typing import *

from pydantic import BaseModel, Field

from .create_task_response_data import CreateTaskResponseData


class CreateTaskResponse(BaseModel):
    """
    None model
    """

    data: Optional[CreateTaskResponseData] = Field(alias="data", default=None)

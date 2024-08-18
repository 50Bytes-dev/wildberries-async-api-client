from typing import *

from pydantic import BaseModel, Field


class CreateTaskResponseData(BaseModel):
    """
    None model
    """

    taskId: Optional[str] = Field(alias="taskId", default=None)

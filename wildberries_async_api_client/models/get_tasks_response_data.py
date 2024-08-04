from typing import *

from pydantic import BaseModel, Field


class GetTasksResponseData(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    status: Optional[str] = Field(alias="status", default=None)

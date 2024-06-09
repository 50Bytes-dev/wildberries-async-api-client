from typing import *

from pydantic import BaseModel, Field

from .EventsResult import EventsResult


class EventsResponse(BaseModel):
    """
    None model

    """

    result: Optional[EventsResult] = Field(alias="result", default=None)

    errors: Optional[Any] = Field(alias="errors", default=None)

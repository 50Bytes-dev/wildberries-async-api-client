from typing import *

from pydantic import BaseModel, Field

from .Event import Event


class EventsResult(BaseModel):
    """
    None model

    """

    next: Optional[int] = Field(alias="next", default=None)

    newestEventTime: Optional[str] = Field(alias="newestEventTime", default=None)

    oldestEventTime: Optional[str] = Field(alias="oldestEventTime", default=None)

    totalEvents: Optional[int] = Field(alias="totalEvents", default=None)

    events: Optional[List[Optional[Event]]] = Field(alias="events", default=None)

from typing import *

from pydantic import BaseModel, Field

from .event_type import EventType
from .refund import Refund
from .sender import Sender


class Event(BaseModel):
    """
    None model

    """

    chatID: Optional[str] = Field(alias="chatID", default=None)

    eventID: Optional[str] = Field(alias="eventID", default=None)

    eventType: Optional[EventType] = Field(alias="eventType", default=None)

    isNewChat: Optional[bool] = Field(alias="isNewChat", default=None)

    message: Optional[Dict[str, Any]] = Field(alias="message", default=None)

    refund: Optional[Refund] = Field(alias="refund", default=None)

    source: Optional[str] = Field(alias="source", default=None)

    addTimestamp: Optional[int] = Field(alias="addTimestamp", default=None)

    addTime: Optional[str] = Field(alias="addTime", default=None)

    replySign: Optional[str] = Field(alias="replySign", default=None)

    sender: Optional[Sender] = Field(alias="sender", default=None)

    clientID: Optional[str] = Field(alias="clientID", default=None)

    clientName: Optional[str] = Field(alias="clientName", default=None)

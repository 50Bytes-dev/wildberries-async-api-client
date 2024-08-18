from typing import *

from pydantic import BaseModel, Field


class Chat(BaseModel):
    """
    None model
    """

    chatID: Optional[str] = Field(alias="chatID", default=None)

    replySign: Optional[str] = Field(alias="replySign", default=None)

    clientID: Optional[str] = Field(alias="clientID", default=None)

    clientName: Optional[str] = Field(alias="clientName", default=None)

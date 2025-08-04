from typing import *

from pydantic import BaseModel, Field

from .good_card import GoodCard


class Chat(BaseModel):
    """
    None model
    """

    chatID: Optional[str] = Field(alias="chatID", default=None)

    replySign: Optional[str] = Field(alias="replySign", default=None)

    clientID: Optional[str] = Field(alias="clientID", default=None)

    clientName: Optional[str] = Field(alias="clientName", default=None)

    goodCard: Optional[GoodCard] = Field(alias="goodCard", default=None)

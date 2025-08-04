from typing import *

from pydantic import BaseModel, Field

from .file import File
from .good_card import GoodCard
from .image import Image


class EventAttachments(BaseModel):
    """
    None model

    Attachments
    """

    goodCard: Optional[GoodCard] = Field(alias="goodCard", default=None)

    files: Optional[List[Optional[File]]] = Field(alias="files", default=None)

    images: Optional[List[Optional[Image]]] = Field(alias="images", default=None)

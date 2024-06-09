from typing import *

from pydantic import BaseModel, Field

from .File import File
from .GoodCard import GoodCard
from .Image import Image


class EventAttachments(BaseModel):
    """
    None model
        Вложения

    """

    goodCard: Optional[GoodCard] = Field(alias="goodCard", default=None)

    files: Optional[List[Optional[File]]] = Field(alias="files", default=None)

    images: Optional[List[Optional[Image]]] = Field(alias="images", default=None)

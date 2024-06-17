from typing import *

from pydantic import BaseModel, Field


class ApiV3OrdersStickersPostResponse(BaseModel):
    """
    None model

    """

    stickers: Optional[List[Dict[str, Any]]] = Field(alias="stickers", default=None)


class Sticker(BaseModel):
    """
    Sticker model

    file: str Полное представление этикетки в заданном формате.  (кодировка base64)

    """

    file: Optional[str] = Field(alias="file", default=None)




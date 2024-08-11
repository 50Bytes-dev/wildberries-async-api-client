from typing import *

from pydantic import BaseModel, Field


class ApiV3FilesOrdersExternalStickersPostResponse(BaseModel):
    """
    None model

    """

    stickers: Optional[List[Dict[str, Any]]] = Field(alias="stickers", default=None)

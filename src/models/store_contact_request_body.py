from typing import *

from pydantic import BaseModel, Field


class StoreContactRequestBody(BaseModel):
    """
    None model

    Seller&#39;s warehouse contacts
    """

    contacts: Optional[List[Dict[str, Any]]] = Field(alias="contacts", default=None)

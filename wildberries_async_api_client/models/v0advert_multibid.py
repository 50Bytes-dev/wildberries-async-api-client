from typing import *

from pydantic import BaseModel, Field

from .v0advert_multi_bid_item import V0advertMultiBidItem


class V0advertMultibid(BaseModel):
    """
    None model
    """

    advert_id: int = Field(alias="advert_id")

    nm_bids: List[V0advertMultiBidItem] = Field(alias="nm_bids")

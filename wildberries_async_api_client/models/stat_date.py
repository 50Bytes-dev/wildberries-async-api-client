from typing import *

from pydantic import BaseModel, Field

from .stats_blok2 import StatsBlok2


class StatDate(BaseModel):
    """
    None model
    """

    dates: Optional[List[str]] = Field(alias="dates", default=None)

    stats: Optional[List[Optional[StatsBlok2]]] = Field(alias="stats", default=None)

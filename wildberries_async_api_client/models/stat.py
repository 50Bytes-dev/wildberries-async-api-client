from typing import *

from pydantic import BaseModel, Field

from .stats_blok1 import StatsBlok1


class Stat(BaseModel):
    """
    None model

    """

    stats: Optional[List[Optional[StatsBlok1]]] = Field(alias="stats", default=None)

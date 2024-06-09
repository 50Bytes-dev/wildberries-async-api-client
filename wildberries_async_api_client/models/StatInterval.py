from typing import *

from pydantic import BaseModel, Field

from .StatsBlok1 import StatsBlok1


class StatInterval(BaseModel):
    """
    None model

    """

    interval: Optional[Dict[str, Any]] = Field(alias="interval", default=None)

    stats: Optional[List[Optional[StatsBlok1]]] = Field(alias="stats", default=None)

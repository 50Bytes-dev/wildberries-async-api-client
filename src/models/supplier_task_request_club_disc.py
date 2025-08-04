from typing import *

from pydantic import BaseModel, Field

from .club_disc import ClubDisc


class SupplierTaskRequestClubDisc(BaseModel):
    """
    None model
    """

    data: Optional[ClubDisc] = Field(alias="data", default=None)

from typing import *

from pydantic import BaseModel, Field

from .club_disc_req import ClubDiscReq

ClubDisc = List[ClubDiscReq]

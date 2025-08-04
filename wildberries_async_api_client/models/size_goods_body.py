from typing import *

from pydantic import BaseModel, Field

from .size_good_req import SizeGoodReq

SizeGoodsBody = List[SizeGoodReq]

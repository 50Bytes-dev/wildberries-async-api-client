from typing import *

from pydantic import BaseModel, Field

from .crossborder_turkey_client_info import CrossborderTurkeyClientInfo


class CrossborderTurkeyClientInfoResp(BaseModel):
    """
    None model
    """

    orders: Optional[List[Optional[CrossborderTurkeyClientInfo]]] = Field(alias="orders", default=None)

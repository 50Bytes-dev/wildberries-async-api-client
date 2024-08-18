from typing import *

from pydantic import BaseModel, Field

from .refund_action_type import RefundActionType


class Refund(BaseModel):
    """
    None model

    Возврат товара
    """

    actionType: Optional[RefundActionType] = Field(alias="actionType", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    priceCurrency: Optional[str] = Field(alias="priceCurrency", default=None)

    rid: Optional[str] = Field(alias="rid", default=None)

from typing import *

from pydantic import BaseModel, Field


class PromotionsSupplierTaskRequest(BaseModel):
    """
    None model
    """

    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)

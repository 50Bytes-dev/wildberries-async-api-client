from typing import *

from pydantic import BaseModel, Field


class CommissionChina(BaseModel):
    """
    None model
    """

    report: Optional[List[Dict[str, Any]]] = Field(alias="report", default=None)

from typing import *

from pydantic import BaseModel, Field

from .supplier_task_metadata import SupplierTaskMetadata


class ResponseTaskHistory(BaseModel):
    """
    None model

    """

    data: Optional[SupplierTaskMetadata] = Field(alias="data", default=None)

    error: Optional[bool] = Field(alias="error", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

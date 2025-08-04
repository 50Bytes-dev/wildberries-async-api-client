from typing import *

from pydantic import BaseModel, Field

from .supplier_task_metadata_buffer import SupplierTaskMetadataBuffer


class ResponseTaskBuffer(BaseModel):
    """
    None model
    """

    data: Optional[SupplierTaskMetadataBuffer] = Field(alias="data", default=None)

    error: Optional[bool] = Field(alias="error", default=None)

    errorText: Optional[str] = Field(alias="errorText", default=None)

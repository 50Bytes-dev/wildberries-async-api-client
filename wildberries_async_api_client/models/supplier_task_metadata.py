from typing import *

from pydantic import BaseModel, Field

from .date import Date
from .date1 import Date1
from .task_status import TaskStatus


class SupplierTaskMetadata(BaseModel):
    """
    None model

    """

    uploadID: Optional[int] = Field(alias="uploadID", default=None)

    status: Optional[TaskStatus] = Field(alias="status", default=None)

    uploadDate: Optional[Date] = Field(alias="uploadDate", default=None)

    activationDate: Optional[Date1] = Field(alias="activationDate", default=None)

    overAllGoodsNumber: Optional[int] = Field(alias="overAllGoodsNumber", default=None)

    successGoodsNumber: Optional[int] = Field(alias="successGoodsNumber", default=None)

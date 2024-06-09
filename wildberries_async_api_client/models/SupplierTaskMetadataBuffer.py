from typing import *

from pydantic import BaseModel, Field

from .Date import Date
from .Date1 import Date1
from .TaskStatusBuffer import TaskStatusBuffer


class SupplierTaskMetadataBuffer(BaseModel):
    """
    None model

    """

    uploadID: Optional[int] = Field(alias="uploadID", default=None)

    status: Optional[TaskStatusBuffer] = Field(alias="status", default=None)

    uploadDate: Optional[Date] = Field(alias="uploadDate", default=None)

    activationDate: Optional[Date1] = Field(alias="activationDate", default=None)

    overAllGoodsNumber: Optional[int] = Field(alias="overAllGoodsNumber", default=None)

    successGoodsNumber: Optional[int] = Field(alias="successGoodsNumber", default=None)

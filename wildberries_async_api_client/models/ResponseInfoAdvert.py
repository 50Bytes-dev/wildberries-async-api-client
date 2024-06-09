from typing import *

from pydantic import BaseModel, Field


class ResponseInfoAdvert(BaseModel):
    """
    None model

    """

    advertId: Optional[int] = Field(alias="advertId", default=None)

    type: Optional[int] = Field(alias="type", default=None)

    status: Optional[int] = Field(alias="status", default=None)

    dailyBudget: Optional[int] = Field(alias="dailyBudget", default=None)

    createTime: Optional[str] = Field(alias="createTime", default=None)

    changeTime: Optional[str] = Field(alias="changeTime", default=None)

    startTime: Optional[str] = Field(alias="startTime", default=None)

    endTime: Optional[str] = Field(alias="endTime", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    params: Optional[List[Dict[str, Any]]] = Field(alias="params", default=None)

    searchPluseState: Optional[bool] = Field(alias="searchPluseState", default=None)

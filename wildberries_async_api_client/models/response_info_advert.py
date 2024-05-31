# coding: utf-8

"""
    Wildberries API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.response_info_advert_params_inner import ResponseInfoAdvertParamsInner
from typing import Optional, Set
from typing_extensions import Self

class ResponseInfoAdvert(BaseModel):
    """
    ResponseInfoAdvert
    """ # noqa: E501
    advert_id: Optional[StrictInt] = Field(default=None, description="Идентификатор кампании", alias="advertId")
    type: Optional[StrictInt] = Field(default=None, description="<dl>   <dt>Тип кампании:</dt>     <dd><code>4</code> - кампания  в каталоге</dd>     <dd><code>5</code> - кампания в карточке товара</dd>     <dd><code>6</code> - кампания в поиске</dd>     <dd><code>7</code> - кампания в рекомендациях на главной странице</dd>   </dl> ")
    status: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Статус кампании:</dt> <dd><code>-1</code> - кампания в процессе удаления </dd> <dd><code>4</code> - готова к запуску </dd> <dd><code>7</code> - Кампания завершена</dd> <dd><code>8</code> - отказался</dd> <dd><code>9</code> - идут показы</dd> <dd><code>11</code> - Кампания на паузе</dd> </dl> Кампания в процессе удаления. Статус означает, что кампания была удалена, и через 3-10 минут она исчезнет из ответа метода.    ")
    daily_budget: Optional[StrictInt] = Field(default=None, description="Дневной бюджет, если не установлен, то 0", alias="dailyBudget")
    create_time: Optional[StrictStr] = Field(default=None, description="Время создания кампании", alias="createTime")
    change_time: Optional[StrictStr] = Field(default=None, description="Время последнего изменения кампании", alias="changeTime")
    start_time: Optional[StrictStr] = Field(default=None, description="Дата последнего запуска кампании", alias="startTime")
    end_time: Optional[StrictStr] = Field(default=None, description="Дата завершения кампании", alias="endTime")
    name: Optional[StrictStr] = Field(default=None, description="Название кампании")
    params: Optional[List[ResponseInfoAdvertParamsInner]] = Field(default=None, description="Параметры кампании")
    search_pluse_state: Optional[StrictBool] = Field(default=None, description="Активность фиксированных фраз (Для кампаний в поиске)  <br> (`false` - отключены, `true` - включены) ", alias="searchPluseState")
    __properties: ClassVar[List[str]] = ["advertId", "type", "status", "dailyBudget", "createTime", "changeTime", "startTime", "endTime", "name", "params", "searchPluseState"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResponseInfoAdvert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in params (list)
        _items = []
        if self.params:
            for _item in self.params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['params'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResponseInfoAdvert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advertId": obj.get("advertId"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "dailyBudget": obj.get("dailyBudget"),
            "createTime": obj.get("createTime"),
            "changeTime": obj.get("changeTime"),
            "startTime": obj.get("startTime"),
            "endTime": obj.get("endTime"),
            "name": obj.get("name"),
            "params": [ResponseInfoAdvertParamsInner.from_dict(_item) for _item in obj["params"]] if obj.get("params") is not None else None,
            "searchPluseState": obj.get("searchPluseState")
        })
        return _obj



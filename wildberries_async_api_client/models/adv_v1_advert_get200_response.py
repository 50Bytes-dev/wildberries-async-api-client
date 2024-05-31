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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.adv_v1_advert_get200_response_extended import AdvV1AdvertGet200ResponseExtended
from wildberries_async_api_client.models.adv_v1_advert_get200_response_items_inner import AdvV1AdvertGet200ResponseItemsInner
from typing import Optional, Set
from typing_extensions import Self

class AdvV1AdvertGet200Response(BaseModel):
    """
    AdvV1AdvertGet200Response
    """ # noqa: E501
    advert_id: Optional[StrictInt] = Field(default=None, description="Идентификатор медиакампании", alias="advertId")
    name: Optional[StrictStr] = Field(default=None, description="Название медиакампании")
    brand: Optional[StrictStr] = Field(default=None, description="Название бренда")
    type: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Тип медиакампании:</dt> <dd><code>1</code> - размещение по дням</dd> <dd><code>2</code> - размещение по просмотрам</dd> </dl> ")
    status: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Статус медиакампании:</dt>   <dd><code>1</code> - черновик</dd>   <dd><code>2</code> - модерация   <dd><code>3</code> - отклонено (с возможностью вернуть на модерацию)</dd>   <dd><code>4</code> - одобрено</dd>   <dd><code>5</code> - запланировано</dd>   <dd><code>6</code> - на показах</dd>   <dd><code>7</code> - завершено</dd>   <dd><code>8</code> - отказался</dd>   <dd><code>9</code> - приостановлена продавцом</dd>   <dd><code>10</code> - пауза по дневному лимиту</dd>   <dd><code>11</code> - пауза по расходу бюджета</dd> </dl> ")
    create_time: Optional[datetime] = Field(default=None, description="Время создания медиакампании", alias="createTime")
    extended: Optional[AdvV1AdvertGet200ResponseExtended] = None
    items: Optional[List[AdvV1AdvertGet200ResponseItemsInner]] = Field(default=None, description="Информация о баннере. <br> Наличие в ответе тех или иных полей зависит от конфигурации медиакампании. ")
    __properties: ClassVar[List[str]] = ["advertId", "name", "brand", "type", "status", "createTime", "extended", "items"]

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
        """Create an instance of AdvV1AdvertGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of extended
        if self.extended:
            _dict['extended'] = self.extended.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvV1AdvertGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advertId": obj.get("advertId"),
            "name": obj.get("name"),
            "brand": obj.get("brand"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "createTime": obj.get("createTime"),
            "extended": AdvV1AdvertGet200ResponseExtended.from_dict(obj["extended"]) if obj.get("extended") is not None else None,
            "items": [AdvV1AdvertGet200ResponseItemsInner.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None
        })
        return _obj



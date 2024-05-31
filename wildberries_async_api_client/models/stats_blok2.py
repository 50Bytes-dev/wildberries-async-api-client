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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wildberries_async_api_client.models.daily_stats2_inner import DailyStats2Inner
from typing import Optional, Set
from typing_extensions import Self

class StatsBlok2(BaseModel):
    """
    StatsBlok2
    """ # noqa: E501
    item_id: Optional[StrictInt] = Field(default=None, description="ID баннера")
    item_name: Optional[StrictStr] = Field(default=None, description="Название бренда")
    category_name: Optional[StrictStr] = Field(default=None, description="Название категории")
    advert_type: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Тип медиакампании:</dt> <dd><code>1</code> - размещение по дням</dd> <dd><code>2</code> - размещение по просмотрам</dd> </dl> ")
    place: Optional[StrictInt] = Field(default=None, description="Место на странице")
    views: Optional[StrictInt] = Field(default=None, description="Количество просмотров")
    clicks: Optional[StrictInt] = Field(default=None, description="Количество кликов")
    cr: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="CR(conversion rate) — это отношение количества заказов к общему количеству посещений медиакампании ")
    ctr: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="CTR (click-through rate) — показатель кликабельности, отношение числа кликов к количеству показов в рамках медиакампании ")
    date_from: Optional[datetime] = Field(default=None, description="Время начала размещения")
    date_to: Optional[datetime] = Field(default=None, description="Время завершения размещения")
    subject_name: Optional[StrictStr] = Field(default=None, description="Родительская категория предмета")
    atbs: Optional[StrictInt] = Field(default=None, description="Количество добавлений товаров в корзину")
    orders: Optional[StrictInt] = Field(default=None, description="Количество заказов")
    price: Optional[StrictInt] = Field(default=None, description="Стоимость размещения")
    cpc: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(cost per click) - цена клика по продвигаемому товару")
    status: Optional[StrictInt] = Field(default=None, description="Статус медиакампании")
    daily_stats: Optional[List[DailyStats2Inner]] = None
    expenses: Optional[StrictInt] = Field(default=None, description="Стоимость размещения баннера")
    cr1: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Отношение количества добавлений в корзину к количеству кликов")
    cr2: Optional[StrictInt] = Field(default=None, description="Отношение количества заказов к количеству добавлений в корзину")
    __properties: ClassVar[List[str]] = ["item_id", "item_name", "category_name", "advert_type", "place", "views", "clicks", "cr", "ctr", "date_from", "date_to", "subject_name", "atbs", "orders", "price", "cpc", "status", "daily_stats", "expenses", "cr1", "cr2"]

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
        """Create an instance of StatsBlok2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in daily_stats (list)
        _items = []
        if self.daily_stats:
            for _item in self.daily_stats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['daily_stats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StatsBlok2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "item_id": obj.get("item_id"),
            "item_name": obj.get("item_name"),
            "category_name": obj.get("category_name"),
            "advert_type": obj.get("advert_type"),
            "place": obj.get("place"),
            "views": obj.get("views"),
            "clicks": obj.get("clicks"),
            "cr": obj.get("cr"),
            "ctr": obj.get("ctr"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "subject_name": obj.get("subject_name"),
            "atbs": obj.get("atbs"),
            "orders": obj.get("orders"),
            "price": obj.get("price"),
            "cpc": obj.get("cpc"),
            "status": obj.get("status"),
            "daily_stats": [DailyStats2Inner.from_dict(_item) for _item in obj["daily_stats"]] if obj.get("daily_stats") is not None else None,
            "expenses": obj.get("expenses"),
            "cr1": obj.get("cr1"),
            "cr2": obj.get("cr2")
        })
        return _obj



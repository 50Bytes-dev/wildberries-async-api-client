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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.stats2_inner import Stats2Inner
from typing import Optional, Set
from typing_extensions import Self

class DailyStats2InnerAppTypeStatsInner(BaseModel):
    """
    DailyStats2InnerAppTypeStatsInner
    """ # noqa: E501
    app_type: Optional[StrictInt] = Field(default=None, description="<dl> <dt>Тип платформы:</dt> <dd><code>1</code> - сайт</dd> <dd><code>32</code> - Android</dd> <dd><code>64</code> - IOS</dd> </dl> ")
    stats: Optional[List[Stats2Inner]] = None
    __properties: ClassVar[List[str]] = ["app_type", "stats"]

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
        """Create an instance of DailyStats2InnerAppTypeStatsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stats (list)
        _items = []
        if self.stats:
            for _item in self.stats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stats'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DailyStats2InnerAppTypeStatsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_type": obj.get("app_type"),
            "stats": [Stats2Inner.from_dict(_item) for _item in obj["stats"]] if obj.get("stats") is not None else None
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ModelsOptionsResultModelResultInnerWarehousesInner(BaseModel):
    """
    ModelsOptionsResultModelResultInnerWarehousesInner
    """ # noqa: E501
    warehouse_id: Optional[StrictInt] = Field(default=None, description="ID склада. По нему можно получить [информацию о складе](./#tag/Informaciya-dlya-formirovaniya-postavok/paths/~1api~1v1~1warehouses/get)", alias="warehouseID")
    can_box: Optional[StrictBool] = Field(default=None, description="Тип упаковки **Короб**:   - `true` — доступен   - `false` — недоступен ", alias="canBox")
    can_monopallet: Optional[StrictBool] = Field(default=None, description="Тип упаковки **Монопаллета**:   - `true` — доступен   - `false` — недоступен ", alias="canMonopallet")
    can_supersafe: Optional[StrictBool] = Field(default=None, description="Тип упаковки **Суперсейф**:   - `true` — доступен   - `false` — недоступен ", alias="canSupersafe")
    __properties: ClassVar[List[str]] = ["warehouseID", "canBox", "canMonopallet", "canSupersafe"]

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
        """Create an instance of ModelsOptionsResultModelResultInnerWarehousesInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelsOptionsResultModelResultInnerWarehousesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "warehouseID": obj.get("warehouseID"),
            "canBox": obj.get("canBox"),
            "canMonopallet": obj.get("canMonopallet"),
            "canSupersafe": obj.get("canSupersafe")
        })
        return _obj



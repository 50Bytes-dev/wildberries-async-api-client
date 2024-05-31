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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.models_warehouse_pallet_rates import ModelsWarehousePalletRates
from typing import Optional, Set
from typing_extensions import Self

class ModelsWarehousesPalletRates(BaseModel):
    """
    ModelsWarehousesPalletRates
    """ # noqa: E501
    dt_from_min: Optional[StrictStr] = Field(default=None, description="Дата начала тарифа", alias="dtFromMin")
    dt_next_pallet: Optional[StrictStr] = Field(default=None, description="Дата начала следующего тарифа", alias="dtNextPallet")
    dt_till_max: Optional[StrictStr] = Field(default=None, description="Дата окончания тарифа", alias="dtTillMax")
    warehouse_list: Optional[List[ModelsWarehousePalletRates]] = Field(default=None, description="Тарифы для монопаллет, сгруппированные по складам", alias="warehouseList")
    __properties: ClassVar[List[str]] = ["dtFromMin", "dtNextPallet", "dtTillMax", "warehouseList"]

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
        """Create an instance of ModelsWarehousesPalletRates from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in warehouse_list (list)
        _items = []
        if self.warehouse_list:
            for _item in self.warehouse_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warehouseList'] = _items
        # set to None if warehouse_list (nullable) is None
        # and model_fields_set contains the field
        if self.warehouse_list is None and "warehouse_list" in self.model_fields_set:
            _dict['warehouseList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelsWarehousesPalletRates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dtFromMin": obj.get("dtFromMin"),
            "dtNextPallet": obj.get("dtNextPallet"),
            "dtTillMax": obj.get("dtTillMax"),
            "warehouseList": [ModelsWarehousePalletRates.from_dict(_item) for _item in obj["warehouseList"]] if obj.get("warehouseList") is not None else None
        })
        return _obj



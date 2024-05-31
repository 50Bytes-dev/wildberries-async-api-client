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
from typing import Optional, Set
from typing_extensions import Self

class ModelsWarehousePalletRates(BaseModel):
    """
    ModelsWarehousePalletRates
    """ # noqa: E501
    pallet_delivery_expr: Optional[StrictStr] = Field(default=None, description="Коэффициент доставки, %. На него умножается стоимость доставки. Во всех тарифах этот коэффициент уже учтён", alias="palletDeliveryExpr")
    pallet_delivery_value_base: Optional[StrictStr] = Field(default=None, description="Доставка 1 литра, ₽", alias="palletDeliveryValueBase")
    pallet_delivery_value_liter: Optional[StrictStr] = Field(default=None, description="Доставка каждого дополнительного литра, ₽", alias="palletDeliveryValueLiter")
    pallet_storage_expr: Optional[StrictStr] = Field(default=None, description="Коэффициент хранения, %. На него умножается стоимость хранения. Во всех тарифах этот коэффициент уже учтён", alias="palletStorageExpr")
    pallet_storage_value_expr: Optional[StrictStr] = Field(default=None, description="Хранение 1 монопаллеты, ₽", alias="palletStorageValueExpr")
    warehouse_name: Optional[StrictStr] = Field(default=None, description="Название склада", alias="warehouseName")
    __properties: ClassVar[List[str]] = ["palletDeliveryExpr", "palletDeliveryValueBase", "palletDeliveryValueLiter", "palletStorageExpr", "palletStorageValueExpr", "warehouseName"]

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
        """Create an instance of ModelsWarehousePalletRates from a JSON string"""
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
        """Create an instance of ModelsWarehousePalletRates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "palletDeliveryExpr": obj.get("palletDeliveryExpr"),
            "palletDeliveryValueBase": obj.get("palletDeliveryValueBase"),
            "palletDeliveryValueLiter": obj.get("palletDeliveryValueLiter"),
            "palletStorageExpr": obj.get("palletStorageExpr"),
            "palletStorageValueExpr": obj.get("palletStorageValueExpr"),
            "warehouseName": obj.get("warehouseName")
        })
        return _obj


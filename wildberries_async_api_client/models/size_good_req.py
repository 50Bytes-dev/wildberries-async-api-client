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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class SizeGoodReq(BaseModel):
    """
    SizeGoodReq
    """ # noqa: E501
    nm_id: StrictInt = Field(description="Артикул Wildberries", alias="nmID")
    size_id: StrictInt = Field(description="ID размера. Можно получить с помощью метода [Получение списка товаров по артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), поле `sizeID`. В методах контента это поле `chrtID`", alias="sizeID")
    price: StrictInt = Field(description="Цена. Валюту можно получить с помощью метода [Получение списка товаров по артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), поле `currencyIsoCode4217`")
    __properties: ClassVar[List[str]] = ["nmID", "sizeID", "price"]

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
        """Create an instance of SizeGoodReq from a JSON string"""
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
        """Create an instance of SizeGoodReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nmID": obj.get("nmID"),
            "sizeID": obj.get("sizeID"),
            "price": obj.get("price")
        })
        return _obj


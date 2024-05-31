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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ContentV2CardsErrorListGet200ResponseDataInner(BaseModel):
    """
    ContentV2CardsErrorListGet200ResponseDataInner
    """ # noqa: E501
    object: Optional[StrictStr] = Field(default=None, description="Категория для который создавалось КТ с данной НМ")
    vendor_code: Optional[StrictStr] = Field(default=None, description="Артикул продавца", alias="vendorCode")
    update_at: Optional[StrictStr] = Field(default=None, description="Дата и время запроса на создание КТ с данным НМ", alias="updateAt")
    errors: Optional[List[StrictStr]] = Field(default=None, description="Список ошибок из-за которых не обработался запрос на создание КТ с данным НМ")
    object_id: Optional[StrictInt] = Field(default=None, description="Идентификатор предмета", alias="objectID")
    __properties: ClassVar[List[str]] = ["object", "vendorCode", "updateAt", "errors", "objectID"]

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
        """Create an instance of ContentV2CardsErrorListGet200ResponseDataInner from a JSON string"""
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
        """Create an instance of ContentV2CardsErrorListGet200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object"),
            "vendorCode": obj.get("vendorCode"),
            "updateAt": obj.get("updateAt"),
            "errors": obj.get("errors"),
            "objectID": obj.get("objectID")
        })
        return _obj



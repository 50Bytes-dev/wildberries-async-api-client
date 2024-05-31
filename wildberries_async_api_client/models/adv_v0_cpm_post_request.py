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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdvV0CpmPostRequest(BaseModel):
    """
    AdvV0CpmPostRequest
    """ # noqa: E501
    advert_id: StrictInt = Field(description="Идентификатор кампании, где меняется ставка", alias="advertId")
    type: StrictInt = Field(description="<dl> <dt>кампании, где меняется ставка:</dt> <dd><code>4</code> - кампания в каталоге </dd>  <dd><code>5</code> - кампания в карточке товара</dd> <dd><code>6</code> - кампания в поиске</dd> <dd><code>7</code> - кампания в рекомендациях на главной странице</dd> <dd><code>8</code> - автоматическая кампания</dd> <dd><code>9</code> - кампания поиск + каталог </dd> </dl> ")
    cpm: StrictInt = Field(description="Новое значение ставки")
    param: StrictInt = Field(description="Параметр, для которого будет внесено изменение. Является значением `subjectId` (для кампании в поиске и рекомендациях), `setId` (для кампании в карточке товара) или `menuId` (для кампании в каталоге).  <br> Для автоматической кампании указывать этот параметр не требуется. ")
    instrument: Optional[StrictInt] = Field(default=None, description="тип кампании для изменения ставки в Поиск + Каталог (4 - каталог, 6 - поиск)")
    __properties: ClassVar[List[str]] = ["advertId", "type", "cpm", "param", "instrument"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([5, 6, 7, 8, 9]):
            raise ValueError("must be one of enum values (5, 6, 7, 8, 9)")
        return value

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
        """Create an instance of AdvV0CpmPostRequest from a JSON string"""
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
        """Create an instance of AdvV0CpmPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advertId": obj.get("advertId"),
            "type": obj.get("type"),
            "cpm": obj.get("cpm"),
            "param": obj.get("param"),
            "instrument": obj.get("instrument")
        })
        return _obj



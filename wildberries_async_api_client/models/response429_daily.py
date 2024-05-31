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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.response_error_additional_errors_inner import ResponseErrorAdditionalErrorsInner
from typing import Optional, Set
from typing_extensions import Self

class Response429Daily(BaseModel):
    """
    Response429Daily
    """ # noqa: E501
    data: Optional[List[Dict[str, Any]]] = None
    error: Optional[StrictBool] = Field(default=None, description="Флаг ошибки")
    error_text: Optional[StrictStr] = Field(default=None, description="Описание ошибки", alias="errorText")
    additional_errors: Optional[List[ResponseErrorAdditionalErrorsInner]] = Field(default=None, description="Дополнительные ошибки", alias="additionalErrors")
    __properties: ClassVar[List[str]] = ["data", "error", "errorText", "additionalErrors"]

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
        """Create an instance of Response429Daily from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in additional_errors (list)
        _items = []
        if self.additional_errors:
            for _item in self.additional_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalErrors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Response429Daily from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": obj.get("data"),
            "error": obj.get("error"),
            "errorText": obj.get("errorText"),
            "additionalErrors": [ResponseErrorAdditionalErrorsInner.from_dict(_item) for _item in obj["additionalErrors"]] if obj.get("additionalErrors") is not None else None
        })
        return _obj



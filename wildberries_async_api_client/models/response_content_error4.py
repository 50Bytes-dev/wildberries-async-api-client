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
from wildberries_async_api_client.models.response_content_error4_additional_errors import ResponseContentError4AdditionalErrors
from typing import Optional, Set
from typing_extensions import Self

class ResponseContentError4(BaseModel):
    """
    ResponseContentError4
    """ # noqa: E501
    data: Optional[Dict[str, Any]] = None
    error: Optional[StrictBool] = Field(default=None, description="Флаг ошибки")
    error_text: Optional[StrictStr] = Field(default=None, description="Описание ошибки", alias="errorText")
    additional_errors: Optional[ResponseContentError4AdditionalErrors] = Field(default=None, alias="additionalErrors")
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
        """Create an instance of ResponseContentError4 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_errors
        if self.additional_errors:
            _dict['additionalErrors'] = self.additional_errors.to_dict()
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResponseContentError4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": obj.get("data"),
            "error": obj.get("error"),
            "errorText": obj.get("errorText"),
            "additionalErrors": ResponseContentError4AdditionalErrors.from_dict(obj["additionalErrors"]) if obj.get("additionalErrors") is not None else None
        })
        return _obj



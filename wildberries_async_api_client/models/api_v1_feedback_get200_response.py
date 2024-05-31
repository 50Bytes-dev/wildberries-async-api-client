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
from wildberries_async_api_client.models.api_v1_feedback_get200_response_data import ApiV1FeedbackGet200ResponseData
from typing import Optional, Set
from typing_extensions import Self

class ApiV1FeedbackGet200Response(BaseModel):
    """
    ApiV1FeedbackGet200Response
    """ # noqa: E501
    data: Optional[ApiV1FeedbackGet200ResponseData] = None
    error: Optional[StrictBool] = Field(default=None, description="Есть ли ошибка")
    error_text: Optional[StrictStr] = Field(default=None, description="Описание ошибки", alias="errorText")
    additional_errors: Optional[List[StrictStr]] = Field(default=None, description="Дополнительные ошибки", alias="additionalErrors")
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
        """Create an instance of ApiV1FeedbackGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # set to None if additional_errors (nullable) is None
        # and model_fields_set contains the field
        if self.additional_errors is None and "additional_errors" in self.model_fields_set:
            _dict['additionalErrors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiV1FeedbackGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": ApiV1FeedbackGet200ResponseData.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "error": obj.get("error"),
            "errorText": obj.get("errorText"),
            "additionalErrors": obj.get("additionalErrors")
        })
        return _obj



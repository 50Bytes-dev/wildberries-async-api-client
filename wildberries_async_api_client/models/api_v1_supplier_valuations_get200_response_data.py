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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.api_v1_supplier_valuations_get200_response_data_feedback_valuations import ApiV1SupplierValuationsGet200ResponseDataFeedbackValuations
from wildberries_async_api_client.models.api_v1_supplier_valuations_get200_response_data_product_valuations import ApiV1SupplierValuationsGet200ResponseDataProductValuations
from typing import Optional, Set
from typing_extensions import Self

class ApiV1SupplierValuationsGet200ResponseData(BaseModel):
    """
    Данные
    """ # noqa: E501
    feedback_valuations: Optional[ApiV1SupplierValuationsGet200ResponseDataFeedbackValuations] = Field(default=None, alias="feedbackValuations")
    product_valuations: Optional[ApiV1SupplierValuationsGet200ResponseDataProductValuations] = Field(default=None, alias="productValuations")
    __properties: ClassVar[List[str]] = ["feedbackValuations", "productValuations"]

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
        """Create an instance of ApiV1SupplierValuationsGet200ResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of feedback_valuations
        if self.feedback_valuations:
            _dict['feedbackValuations'] = self.feedback_valuations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_valuations
        if self.product_valuations:
            _dict['productValuations'] = self.product_valuations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiV1SupplierValuationsGet200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "feedbackValuations": ApiV1SupplierValuationsGet200ResponseDataFeedbackValuations.from_dict(obj["feedbackValuations"]) if obj.get("feedbackValuations") is not None else None,
            "productValuations": ApiV1SupplierValuationsGet200ResponseDataProductValuations.from_dict(obj["productValuations"]) if obj.get("productValuations") is not None else None
        })
        return _obj



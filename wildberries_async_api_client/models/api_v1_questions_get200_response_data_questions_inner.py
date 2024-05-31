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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.api_v1_questions_get200_response_data_questions_inner_answer import ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer
from wildberries_async_api_client.models.api_v1_questions_get200_response_data_questions_inner_product_details import ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails
from typing import Optional, Set
from typing_extensions import Self

class ApiV1QuestionsGet200ResponseDataQuestionsInner(BaseModel):
    """
    ApiV1QuestionsGet200ResponseDataQuestionsInner
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id вопроса")
    text: Optional[StrictStr] = Field(default=None, description="Текст вопроса")
    created_date: Optional[datetime] = Field(default=None, description="Дата и время создания вопроса", alias="createdDate")
    state: Optional[StrictStr] = Field(default=None, description="Статус вопроса:   - `none` - вопрос отклонён продавцом (такой вопрос не отображается на портале покупателей)   - `wbRu` - ответ предоставлен, вопрос отображается на сайте покупателей   - `suppliersPortalSynch` - новый вопрос ")
    answer: Optional[ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer] = None
    product_details: Optional[ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails] = Field(default=None, alias="productDetails")
    was_viewed: Optional[StrictBool] = Field(default=None, description="Просмотрен ли вопрос", alias="wasViewed")
    __properties: ClassVar[List[str]] = ["id", "text", "createdDate", "state", "answer", "productDetails", "wasViewed"]

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
        """Create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of answer
        if self.answer:
            _dict['answer'] = self.answer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_details
        if self.product_details:
            _dict['productDetails'] = self.product_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "text": obj.get("text"),
            "createdDate": obj.get("createdDate"),
            "state": obj.get("state"),
            "answer": ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer.from_dict(obj["answer"]) if obj.get("answer") is not None else None,
            "productDetails": ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails.from_dict(obj["productDetails"]) if obj.get("productDetails") is not None else None,
            "wasViewed": obj.get("wasViewed")
        })
        return _obj



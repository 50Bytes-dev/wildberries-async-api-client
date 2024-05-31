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
from wildberries_async_api_client.models.adv_v1_stat_words_get200_response_words_keywords_inner import AdvV1StatWordsGet200ResponseWordsKeywordsInner
from typing import Optional, Set
from typing_extensions import Self

class AdvV1StatWordsGet200ResponseWords(BaseModel):
    """
    Блок информации по ключевым фразам
    """ # noqa: E501
    phrase: Optional[List[StrictStr]] = Field(default=None, description="Фразовое соответствие (минус фразы)")
    strong: Optional[List[StrictStr]] = Field(default=None, description="Точное соответствие (минус фразы)")
    excluded: Optional[List[StrictStr]] = Field(default=None, description="Минус фразы из поиска")
    pluse: Optional[List[StrictStr]] = Field(default=None, description="Фиксированные фразы")
    keywords: Optional[List[AdvV1StatWordsGet200ResponseWordsKeywordsInner]] = Field(default=None, description="Блок со статистикой по ключевым фразам")
    fixed: Optional[StrictBool] = Field(default=None, description="Фиксированные ключевые фразы (`true` - включены, `false` - выключены) ")
    __properties: ClassVar[List[str]] = ["phrase", "strong", "excluded", "pluse", "keywords", "fixed"]

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
        """Create an instance of AdvV1StatWordsGet200ResponseWords from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in keywords (list)
        _items = []
        if self.keywords:
            for _item in self.keywords:
                if _item:
                    _items.append(_item.to_dict())
            _dict['keywords'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdvV1StatWordsGet200ResponseWords from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "phrase": obj.get("phrase"),
            "strong": obj.get("strong"),
            "excluded": obj.get("excluded"),
            "pluse": obj.get("pluse"),
            "keywords": [AdvV1StatWordsGet200ResponseWordsKeywordsInner.from_dict(_item) for _item in obj["keywords"]] if obj.get("keywords") is not None else None,
            "fixed": obj.get("fixed")
        })
        return _obj



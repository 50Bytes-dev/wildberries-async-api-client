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

class ApiV1FeedbackGet200ResponseDataProductDetails(BaseModel):
    """
    Структура товара
    """ # noqa: E501
    nm_id: Optional[StrictInt] = Field(default=None, description="Артикул WB", alias="nmId")
    imt_id: Optional[StrictInt] = Field(default=None, description="Идентификатор карточки товара", alias="imtId")
    product_name: Optional[StrictStr] = Field(default=None, description="Название товара", alias="productName")
    supplier_article: Optional[StrictStr] = Field(default=None, description="Артикул продавца", alias="supplierArticle")
    supplier_name: Optional[StrictStr] = Field(default=None, description="Имя продавца", alias="supplierName")
    brand_name: Optional[StrictStr] = Field(default=None, description="Бренд товара", alias="brandName")
    size: Optional[StrictStr] = Field(default=None, description="Размер товара (`techSize` в КТ)")
    __properties: ClassVar[List[str]] = ["nmId", "imtId", "productName", "supplierArticle", "supplierName", "brandName", "size"]

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
        """Create an instance of ApiV1FeedbackGet200ResponseDataProductDetails from a JSON string"""
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
        # set to None if supplier_article (nullable) is None
        # and model_fields_set contains the field
        if self.supplier_article is None and "supplier_article" in self.model_fields_set:
            _dict['supplierArticle'] = None

        # set to None if supplier_name (nullable) is None
        # and model_fields_set contains the field
        if self.supplier_name is None and "supplier_name" in self.model_fields_set:
            _dict['supplierName'] = None

        # set to None if brand_name (nullable) is None
        # and model_fields_set contains the field
        if self.brand_name is None and "brand_name" in self.model_fields_set:
            _dict['brandName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiV1FeedbackGet200ResponseDataProductDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nmId": obj.get("nmId"),
            "imtId": obj.get("imtId"),
            "productName": obj.get("productName"),
            "supplierArticle": obj.get("supplierArticle"),
            "supplierName": obj.get("supplierName"),
            "brandName": obj.get("brandName"),
            "size": obj.get("size")
        })
        return _obj



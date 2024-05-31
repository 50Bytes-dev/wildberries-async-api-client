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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wildberries_async_api_client.models.content_v2_cards_upload_add_post_request_cards_to_add_inner_characteristics_inner import ContentV2CardsUploadAddPostRequestCardsToAddInnerCharacteristicsInner
from wildberries_async_api_client.models.content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner import ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner
from wildberries_async_api_client.models.content_v2_cards_upload_post_request_inner_variants_inner_dimensions import ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions
from typing import Optional, Set
from typing_extensions import Self

class ContentV2CardsUploadAddPostRequestCardsToAddInner(BaseModel):
    """
    ContentV2CardsUploadAddPostRequestCardsToAddInner
    """ # noqa: E501
    brand: Optional[StrictStr] = Field(default=None, description="Бренд")
    vendor_code: StrictStr = Field(description="Артикул продавца", alias="vendorCode")
    title: Optional[StrictStr] = Field(default=None, description="Наименование товара")
    description: Optional[StrictStr] = Field(default=None, description="Описание товара. Максимальное количество символов зависит от категории товара. Стандарт — 2000, минимум — 1000, максимум — 5000.<br> Подробно о правилах описания в **Правилах заполнения карточки товара** в разделе [Инструкции](https://seller.wildberries.ru/training) на портале продавцов. ")
    dimensions: Optional[ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions] = None
    characteristics: Optional[List[ContentV2CardsUploadAddPostRequestCardsToAddInnerCharacteristicsInner]] = Field(default=None, description="Характеристики товара")
    sizes: Optional[List[ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner]] = Field(default=None, description="Массив с размерами. <br>  Если для размерного товара (обувь, одежда и др.) не указать этот массив, то системой в карточке он будет сгенерирован автоматически с `techSize` = \"A\" и `wbSize` = \"1\" и баркодом. ")
    __properties: ClassVar[List[str]] = ["brand", "vendorCode", "title", "description", "dimensions", "characteristics", "sizes"]

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
        """Create an instance of ContentV2CardsUploadAddPostRequestCardsToAddInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of dimensions
        if self.dimensions:
            _dict['dimensions'] = self.dimensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in characteristics (list)
        _items = []
        if self.characteristics:
            for _item in self.characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['characteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sizes (list)
        _items = []
        if self.sizes:
            for _item in self.sizes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sizes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentV2CardsUploadAddPostRequestCardsToAddInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brand": obj.get("brand"),
            "vendorCode": obj.get("vendorCode"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "dimensions": ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions.from_dict(obj["dimensions"]) if obj.get("dimensions") is not None else None,
            "characteristics": [ContentV2CardsUploadAddPostRequestCardsToAddInnerCharacteristicsInner.from_dict(_item) for _item in obj["characteristics"]] if obj.get("characteristics") is not None else None,
            "sizes": [ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner.from_dict(_item) for _item in obj["sizes"]] if obj.get("sizes") is not None else None
        })
        return _obj



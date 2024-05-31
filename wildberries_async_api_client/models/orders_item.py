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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OrdersItem(BaseModel):
    """
    OrdersItem
    """ # noqa: E501
    var_date: Optional[datetime] = Field(default=None, description="Дата и время заказа. Это поле соответствует параметру `dateFrom` в запросе, если параметр `flag`=1. Если часовой пояс не указан, то берется Московское время (UTC+3).", alias="date")
    last_change_date: Optional[datetime] = Field(default=None, description="Дата и время обновления информации в сервисе. Это поле соответствует параметру `dateFrom` в запросе, если параметр `flag`=0 или не указан. Если часовой пояс не указан, то берется Московское время (UTC+3).", alias="lastChangeDate")
    warehouse_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Склад отгрузки", alias="warehouseName")
    country_name: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="Страна", alias="countryName")
    oblast_okrug_name: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="Округ", alias="oblastOkrugName")
    region_name: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="Регион", alias="regionName")
    supplier_article: Optional[Annotated[str, Field(strict=True, max_length=75)]] = Field(default=None, description="Артикул продавца", alias="supplierArticle")
    nm_id: Optional[StrictInt] = Field(default=None, description="Артикул WB", alias="nmId")
    barcode: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="Баркод")
    category: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Категория")
    subject: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Предмет")
    brand: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Бренд")
    tech_size: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="Размер товара", alias="techSize")
    income_id: Optional[StrictInt] = Field(default=None, description="Номер поставки", alias="incomeID")
    is_supply: Optional[StrictBool] = Field(default=None, description="Договор поставки", alias="isSupply")
    is_realization: Optional[StrictBool] = Field(default=None, description="Договор реализации", alias="isRealization")
    total_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Цена без скидок", alias="totalPrice")
    discount_percent: Optional[StrictInt] = Field(default=None, description="Скидка продавца", alias="discountPercent")
    spp: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Скидка WB")
    finished_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Цена с учетом всех скидок, кроме суммы по WB Кошельку", alias="finishedPrice")
    price_with_disc: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Цена со скидкой продавца (= `totalPrice` * (1 - `discountPercent`/100))", alias="priceWithDisc")
    is_cancel: Optional[StrictBool] = Field(default=None, description="Отмена заказа. true - заказ отменен", alias="isCancel")
    cancel_date: Optional[datetime] = Field(default=None, description="Дата и время отмены заказа. Если заказ не был отменен, то \"0001-01-01T00:00:00\".Если часовой пояс не указан, то берется Московское время UTC+3.", alias="cancelDate")
    order_type: Optional[StrictStr] = Field(default=None, description="Тип заказа <ul> <li> `Клиентский` — заказ, поступивший от покупателя <li> `Возврат Брака` — возврат товара продавцу <li> `Принудительный возврат` — возврат товара продавцу <li> `Возврат обезлички` — возврат товара продавцу <li> `Возврат Неверного Вложения` — возврат товара продавцу <li> `Возврат Продавца` — возврат товара продавцу </ul> ", alias="orderType")
    sticker: Optional[StrictStr] = Field(default=None, description="Идентификатор стикера")
    g_number: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Номер заказа", alias="gNumber")
    srid: Optional[StrictStr] = Field(default=None, description="Уникальный идентификатор заказа.<br> Примечание для использующих API Маркетплейс: `srid` равен `rid` в ответах методов сборочных заданий. ")
    __properties: ClassVar[List[str]] = ["date", "lastChangeDate", "warehouseName", "countryName", "oblastOkrugName", "regionName", "supplierArticle", "nmId", "barcode", "category", "subject", "brand", "techSize", "incomeID", "isSupply", "isRealization", "totalPrice", "discountPercent", "spp", "finishedPrice", "priceWithDisc", "isCancel", "cancelDate", "orderType", "sticker", "gNumber", "srid"]

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
        """Create an instance of OrdersItem from a JSON string"""
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
        """Create an instance of OrdersItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "lastChangeDate": obj.get("lastChangeDate"),
            "warehouseName": obj.get("warehouseName"),
            "countryName": obj.get("countryName"),
            "oblastOkrugName": obj.get("oblastOkrugName"),
            "regionName": obj.get("regionName"),
            "supplierArticle": obj.get("supplierArticle"),
            "nmId": obj.get("nmId"),
            "barcode": obj.get("barcode"),
            "category": obj.get("category"),
            "subject": obj.get("subject"),
            "brand": obj.get("brand"),
            "techSize": obj.get("techSize"),
            "incomeID": obj.get("incomeID"),
            "isSupply": obj.get("isSupply"),
            "isRealization": obj.get("isRealization"),
            "totalPrice": obj.get("totalPrice"),
            "discountPercent": obj.get("discountPercent"),
            "spp": obj.get("spp"),
            "finishedPrice": obj.get("finishedPrice"),
            "priceWithDisc": obj.get("priceWithDisc"),
            "isCancel": obj.get("isCancel"),
            "cancelDate": obj.get("cancelDate"),
            "orderType": obj.get("orderType"),
            "sticker": obj.get("sticker"),
            "gNumber": obj.get("gNumber"),
            "srid": obj.get("srid")
        })
        return _obj



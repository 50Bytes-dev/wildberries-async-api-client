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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class BySelectedNmIDReqParams(BaseModel):
    """
    Параметры отчёта
    """ # noqa: E501
    nm_ids: Optional[Annotated[List[StrictInt], Field(min_length=0, max_length=1000)]] = Field(default=None, description="`nmID `, по которым составить отчёт. Оставьте пустым, чтобы получить отчёт по всем товарам ", alias="nmIDs")
    subject_ids: Optional[List[StrictInt]] = Field(default=None, description="Идентификаторы предметов", alias="subjectIDs")
    brand_names: Optional[List[StrictStr]] = Field(default=None, description="Бренды", alias="brandNames")
    tag_ids: Optional[List[StrictInt]] = Field(default=None, description="Идентификаторы тегов", alias="tagIDs")
    start_date: date = Field(description="Начало периода", alias="startDate")
    end_date: date = Field(description="Конец периода", alias="endDate")
    timezone: Optional[StrictStr] = Field(default=None, description="Временная зона, по умолчанию Europe/Moscow ")
    aggregation_level: Optional[StrictStr] = Field(default=None, description="Как сгруппировать данные (по умолчанию по дням):    * `day` — по дням   * `week` — по неделям   * `month` — по месяцам ", alias="aggregationLevel")
    skip_deleted_nm: Optional[StrictBool] = Field(default=None, description="Скрыть удалённые номенклатуры", alias="skipDeletedNm")
    __properties: ClassVar[List[str]] = ["nmIDs", "subjectIDs", "brandNames", "tagIDs", "startDate", "endDate", "timezone", "aggregationLevel", "skipDeletedNm"]

    @field_validator('aggregation_level')
    def aggregation_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['day', 'week', 'month']):
            raise ValueError("must be one of enum values ('day', 'week', 'month')")
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
        """Create an instance of BySelectedNmIDReqParams from a JSON string"""
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
        """Create an instance of BySelectedNmIDReqParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nmIDs": obj.get("nmIDs"),
            "subjectIDs": obj.get("subjectIDs"),
            "brandNames": obj.get("brandNames"),
            "tagIDs": obj.get("tagIDs"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "timezone": obj.get("timezone"),
            "aggregationLevel": obj.get("aggregationLevel"),
            "skipDeletedNm": obj.get("skipDeletedNm")
        })
        return _obj



from typing import *

from pydantic import BaseModel, Field


class Supply(BaseModel):
    """
    Model for Supply

    id: str Идентификатор поставки
    done: bool Флаг закрытия поставки
    createdAt: date-time Дата создания поставки (RFC3339)
    closedAt: date-time Дата закрытия поставки  (RFC3339)
    scanDt: date-time Дата сканирования поставки  (RFC3339)
    name: str Наименование поставки
    cargoType: int Тип поставки
                0 - признак отсутствует
                1 - обычная
                2 - СГТ (Содержит сверхгабаритные товары)
                3 - КГТ (Содержит крупногабаритные товары). Не используется на данный момент

    """

    id: Optional[str] = Field(alias="id", default=None)

    done: Optional[bool] = Field(alias="done", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    closedAt: Optional[str] = Field(alias="closedAt", default=None)

    scanDt: Optional[str] = Field(alias="scanDt", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

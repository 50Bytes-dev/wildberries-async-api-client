from typing import *

from pydantic import BaseModel, Field


class OrderNew(BaseModel):
    """
    Model for new order from API

    id: Идентификатор сборочного задания в Маркетплейсе
    rid: Идентификатор сборочного задания в системе Wildberries
    createdAt: Дата создания сборочного задания (RFC3339)
    warehouseId: Идентификатор склада продавца, на который поступило сборочное задание
    offices: Список офисов, куда следует привезти товар
    address: Детализованный адрес покупателя для доставки (если применимо).
    requiredMeta: Перечень метаданных, которые необходимо добавить в сборочное задание.
    user: Информация о покупателе (только для доставки силами продавца)
    skus: Массив баркодов товара
    price: Цена в валюте продажи с учетом всех скидок, умноженная на 100
    convertedPrice: Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100.
    currencyCode: Код валюты продажи (ISO 4217)
    convertedCurrencyCode: Код валюты страны продавца (ISO 4217)
    orderUid: Идентификатор транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID
    deliveryType: Тип доставки:
                    fbs - доставка на склад Wildberries
                    dbs - доставка силами продавца
                    edbs - экспресс-доставка силами продавца
                    wbgo - доставка курьером WB
    nmId: Артикул WB
    chrtId: Идентификатор размера товара в системе Wildberries
    article: Артикул продавца
    colorCode: Код цвета (только для колеруемых товаров)
    cargoType: Тип товара:
                    1 - обычный
                    2 - СГТ (Сверхгабаритный товар)
                    3 - КГТ (Крупногабаритный товар). Не используется на данный момент.
    """

    id: Optional[int] = Field(alias="id", default=None)

    rid: Optional[str] = Field(alias="rid", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    warehouseId: Optional[int] = Field(alias="warehouseId", default=None)

    offices: Optional[List[str]] = Field(alias="offices", default=None)

    address: Optional[Dict[str, Any]] = Field(alias="address", default=None)

    requiredMeta: Optional[List[str]] = Field(alias="requiredMeta", default=None)

    user: Optional[Dict[str, Any]] = Field(alias="user", default=None)

    skus: Optional[List[str]] = Field(alias="skus", default=None)

    price: Optional[int] = Field(alias="price", default=None)

    convertedPrice: Optional[int] = Field(alias="convertedPrice", default=None)

    currencyCode: Optional[int] = Field(alias="currencyCode", default=None)

    convertedCurrencyCode: Optional[int] = Field(alias="convertedCurrencyCode", default=None)

    orderUid: Optional[str] = Field(alias="orderUid", default=None)

    deliveryType: Optional[str] = Field(alias="deliveryType", default=None)

    nmId: Optional[int] = Field(alias="nmId", default=None)

    chrtId: Optional[int] = Field(alias="chrtId", default=None)

    article: Optional[str] = Field(alias="article", default=None)

    colorCode: Optional[str] = Field(alias="colorCode", default=None)

    cargoType: Optional[int] = Field(alias="cargoType", default=None)

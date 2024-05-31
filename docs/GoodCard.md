# GoodCard

Информация о заказе

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Дата заказа | [optional] 
**need_refund** | **bool** | Запрошен ли возврат товара:  - &#x60;false&#x60; — не запрошен - &#x60;true&#x60; — запрошен  | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**price** | **int** | Стоимость заказа | [optional] 
**price_currency** | **str** | Валюта | [optional] 
**rid** | **str** | Уникальный ID заказа в WB | [optional] 
**size** | **str** | Размер товара | [optional] 
**status_id** | **int** | Статус товара: - &#x60;0&#x60; — Товар активный - &#x60;1&#x60; — Товар оформлен - &#x60;2&#x60; — Товар собирается  - &#x60;3&#x60; — Товар в пути - &#x60;4&#x60; — Товар ожидает в ПВЗ  - &#x60;5&#x60; — Товар у курьера - &#x60;10&#x60; — Товар в архиве  - &#x60;11&#x60; — Товар выкуплен  - &#x60;12&#x60; — Товар отменён  - &#x60;13&#x60; — Оформлен возврат  - &#x60;14&#x60; — Товар отменён (нет на складе)  | [optional] 

## Example

```python
from wildberries_async_api_client.models.good_card import GoodCard

# TODO update the JSON string below
json = "{}"
# create an instance of GoodCard from a JSON string
good_card_instance = GoodCard.from_json(json)
# print the JSON string representation of the object
print(GoodCard.to_json())

# convert the object into a dict
good_card_dict = good_card_instance.to_dict()
# create an instance of GoodCard from a dict
good_card_from_dict = GoodCard.from_dict(good_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



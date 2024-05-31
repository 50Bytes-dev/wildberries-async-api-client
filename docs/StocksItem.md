# StocksItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_change_date** | **datetime** | Дата и время обновления информации в сервисе. Это поле соответствует параметру &#x60;dateFrom&#x60; в запросе. Если часовой пояс не указан, то берется Московское время (UTC+3) | [optional] 
**warehouse_name** | **str** | Название склада | [optional] 
**supplier_article** | **str** | Артикул продавца | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**barcode** | **str** | Баркод | [optional] 
**quantity** | **int** | Количество, доступное для продажи (сколько можно добавить в корзину) | [optional] 
**in_way_to_client** | **int** | В пути к клиенту | [optional] 
**in_way_from_client** | **int** | В пути от клиента | [optional] 
**quantity_full** | **int** | Полное (непроданное) количество, которое числится за складом (&#x3D; &#x60;quantity&#x60; + в пути) | [optional] 
**category** | **str** | Категория | [optional] 
**subject** | **str** | Предмет | [optional] 
**brand** | **str** | Бренд | [optional] 
**tech_size** | **str** | Размер | [optional] 
**price** | **float** | Цена | [optional] 
**discount** | **float** | Скидка | [optional] 
**is_supply** | **bool** | Договор поставки (внутренние технологические данные) | [optional] 
**is_realization** | **bool** | Договор реализации (внутренние технологические данные) | [optional] 
**sc_code** | **str** | Код контракта (внутренние технологические данные) | [optional] 

## Example

```python
from wildberries_async_api_client.models.stocks_item import StocksItem

# TODO update the JSON string below
json = "{}"
# create an instance of StocksItem from a JSON string
stocks_item_instance = StocksItem.from_json(json)
# print the JSON string representation of the object
print(StocksItem.to_json())

# convert the object into a dict
stocks_item_dict = stocks_item_instance.to_dict()
# create an instance of StocksItem from a dict
stocks_item_from_dict = StocksItem.from_dict(stocks_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



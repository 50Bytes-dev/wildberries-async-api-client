# IncomesItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**income_id** | **int** | Номер поставки | [optional] 
**number** | **str** | Номер УПД | [optional] 
**var_date** | **date** | Дата поступления. Если часовой пояс не указан, то берется Московское время UTC+3. | [optional] 
**last_change_date** | **datetime** | Дата и время обновления информации в сервисе. Это поле соответствует параметру &#x60;dateFrom&#x60; в запросе. Если часовой пояс не указан, то берется Московское время UTC+3. | [optional] 
**supplier_article** | **str** | Артикул продавца | [optional] 
**tech_size** | **str** | Размер товара (пример S, M, L, XL, 42, 42-43) | [optional] 
**barcode** | **str** | Бар-код | [optional] 
**quantity** | **int** | Количество | [optional] 
**total_price** | **float** | Цена из УПД | [optional] 
**date_close** | **date** | Дата принятия (закрытия) в WB. Если часовой пояс не указан, то берется Московское время UTC+3 | [optional] 
**warehouse_name** | **str** | Название склада | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**status** | **str** | Текущий статус поставки | [optional] 

## Example

```python
from wildberries_async_api_client.models.incomes_item import IncomesItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomesItem from a JSON string
incomes_item_instance = IncomesItem.from_json(json)
# print the JSON string representation of the object
print(IncomesItem.to_json())

# convert the object into a dict
incomes_item_dict = incomes_item_instance.to_dict()
# create an instance of IncomesItem from a dict
incomes_item_from_dict = IncomesItem.from_dict(incomes_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



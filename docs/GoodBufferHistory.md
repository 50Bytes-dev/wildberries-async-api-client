# GoodBufferHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**size_id** | **int** | ID размера. В методах контента это поле &#x60;chrtID&#x60; | [optional] 
**tech_size_name** | **str** | Размер | [optional] 
**price** | **int** | Цена | [optional] 
**currency_iso_code4217** | **str** | Валюта, по стандарту ISO 4217 | [optional] 
**discount** | **int** | Скидка, % | [optional] 
**status** | **int** | Статус товара: &#x60;1&#x60; — в обработке  | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.good_buffer_history import GoodBufferHistory

# TODO update the JSON string below
json = "{}"
# create an instance of GoodBufferHistory from a JSON string
good_buffer_history_instance = GoodBufferHistory.from_json(json)
# print the JSON string representation of the object
print(GoodBufferHistory.to_json())

# convert the object into a dict
good_buffer_history_dict = good_buffer_history_instance.to_dict()
# create an instance of GoodBufferHistory from a dict
good_buffer_history_from_dict = GoodBufferHistory.from_dict(good_buffer_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



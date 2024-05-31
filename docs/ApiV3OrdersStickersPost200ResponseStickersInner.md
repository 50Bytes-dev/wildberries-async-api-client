# ApiV3OrdersStickersPost200ResponseStickersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Идентификатор сборочного задания | [optional] 
**part_a** | **int** | Первая часть идентификатора этикетки (для печати подписи) | [optional] 
**part_b** | **int** | Вторая часть идентификатора этикетки | [optional] 
**barcode** | **str** | Закодированное значение этикетки | [optional] 
**file** | **bytearray** | Полное представление этикетки в заданном формате. (кодировка base64) | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_orders_stickers_post200_response_stickers_inner import ApiV3OrdersStickersPost200ResponseStickersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersStickersPost200ResponseStickersInner from a JSON string
api_v3_orders_stickers_post200_response_stickers_inner_instance = ApiV3OrdersStickersPost200ResponseStickersInner.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersStickersPost200ResponseStickersInner.to_json())

# convert the object into a dict
api_v3_orders_stickers_post200_response_stickers_inner_dict = api_v3_orders_stickers_post200_response_stickers_inner_instance.to_dict()
# create an instance of ApiV3OrdersStickersPost200ResponseStickersInner from a dict
api_v3_orders_stickers_post200_response_stickers_inner_from_dict = ApiV3OrdersStickersPost200ResponseStickersInner.from_dict(api_v3_orders_stickers_post200_response_stickers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



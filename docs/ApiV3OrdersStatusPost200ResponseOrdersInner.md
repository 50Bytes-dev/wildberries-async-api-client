# ApiV3OrdersStatusPost200ResponseOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор сборочного задания | [optional] 
**supplier_status** | **str** | Статус сборочного задания продавца (устанавливается продавцом) | [optional] 
**wb_status** | **str** | Статус сборочного задания в системе Wildberries | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_orders_status_post200_response_orders_inner import ApiV3OrdersStatusPost200ResponseOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersStatusPost200ResponseOrdersInner from a JSON string
api_v3_orders_status_post200_response_orders_inner_instance = ApiV3OrdersStatusPost200ResponseOrdersInner.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersStatusPost200ResponseOrdersInner.to_json())

# convert the object into a dict
api_v3_orders_status_post200_response_orders_inner_dict = api_v3_orders_status_post200_response_orders_inner_instance.to_dict()
# create an instance of ApiV3OrdersStatusPost200ResponseOrdersInner from a dict
api_v3_orders_status_post200_response_orders_inner_from_dict = ApiV3OrdersStatusPost200ResponseOrdersInner.from_dict(api_v3_orders_status_post200_response_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV3OrdersGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **int** | Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения следующего пакета данных | [optional] 
**orders** | [**List[Order]**](Order.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_orders_get200_response import ApiV3OrdersGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersGet200Response from a JSON string
api_v3_orders_get200_response_instance = ApiV3OrdersGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersGet200Response.to_json())

# convert the object into a dict
api_v3_orders_get200_response_dict = api_v3_orders_get200_response_instance.to_dict()
# create an instance of ApiV3OrdersGet200Response from a dict
api_v3_orders_get200_response_from_dict = ApiV3OrdersGet200Response.from_dict(api_v3_orders_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



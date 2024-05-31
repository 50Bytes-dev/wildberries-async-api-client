# ApiV3OrdersNewGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[OrderNew]**](OrderNew.md) | Список новых сборочных заданий | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_orders_new_get200_response import ApiV3OrdersNewGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersNewGet200Response from a JSON string
api_v3_orders_new_get200_response_instance = ApiV3OrdersNewGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersNewGet200Response.to_json())

# convert the object into a dict
api_v3_orders_new_get200_response_dict = api_v3_orders_new_get200_response_instance.to_dict()
# create an instance of ApiV3OrdersNewGet200Response from a dict
api_v3_orders_new_get200_response_from_dict = ApiV3OrdersNewGet200Response.from_dict(api_v3_orders_new_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



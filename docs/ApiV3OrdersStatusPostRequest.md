# ApiV3OrdersStatusPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | **List[int]** | Список идентификаторов сборочных заданий | 

## Example

```python
from wildberries_async_api_client.models.api_v3_orders_status_post_request import ApiV3OrdersStatusPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersStatusPostRequest from a JSON string
api_v3_orders_status_post_request_instance = ApiV3OrdersStatusPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersStatusPostRequest.to_json())

# convert the object into a dict
api_v3_orders_status_post_request_dict = api_v3_orders_status_post_request_instance.to_dict()
# create an instance of ApiV3OrdersStatusPostRequest from a dict
api_v3_orders_status_post_request_from_dict = ApiV3OrdersStatusPostRequest.from_dict(api_v3_orders_status_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



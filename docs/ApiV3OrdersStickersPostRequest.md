# ApiV3OrdersStickersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | **List[int]** | Массив идентификаторов сборочных заданий | [optional] 

## Example

```python
from wb_client.models.api_v3_orders_stickers_post_request import ApiV3OrdersStickersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersStickersPostRequest from a JSON string
api_v3_orders_stickers_post_request_instance = ApiV3OrdersStickersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersStickersPostRequest.to_json())

# convert the object into a dict
api_v3_orders_stickers_post_request_dict = api_v3_orders_stickers_post_request_instance.to_dict()
# create an instance of ApiV3OrdersStickersPostRequest from a dict
api_v3_orders_stickers_post_request_from_dict = ApiV3OrdersStickersPostRequest.from_dict(api_v3_orders_stickers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



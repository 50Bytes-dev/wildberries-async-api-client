# ApiV3OrdersStickersPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stickers** | [**List[ApiV3OrdersStickersPost200ResponseStickersInner]**](ApiV3OrdersStickersPost200ResponseStickersInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_orders_stickers_post200_response import ApiV3OrdersStickersPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersStickersPost200Response from a JSON string
api_v3_orders_stickers_post200_response_instance = ApiV3OrdersStickersPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersStickersPost200Response.to_json())

# convert the object into a dict
api_v3_orders_stickers_post200_response_dict = api_v3_orders_stickers_post200_response_instance.to_dict()
# create an instance of ApiV3OrdersStickersPost200Response from a dict
api_v3_orders_stickers_post200_response_from_dict = ApiV3OrdersStickersPost200Response.from_dict(api_v3_orders_stickers_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



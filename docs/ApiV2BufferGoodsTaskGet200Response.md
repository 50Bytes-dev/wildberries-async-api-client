# ApiV2BufferGoodsTaskGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV2BufferGoodsTaskGet200ResponseData**](ApiV2BufferGoodsTaskGet200ResponseData.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_buffer_goods_task_get200_response import ApiV2BufferGoodsTaskGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2BufferGoodsTaskGet200Response from a JSON string
api_v2_buffer_goods_task_get200_response_instance = ApiV2BufferGoodsTaskGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2BufferGoodsTaskGet200Response.to_json())

# convert the object into a dict
api_v2_buffer_goods_task_get200_response_dict = api_v2_buffer_goods_task_get200_response_instance.to_dict()
# create an instance of ApiV2BufferGoodsTaskGet200Response from a dict
api_v2_buffer_goods_task_get200_response_from_dict = ApiV2BufferGoodsTaskGet200Response.from_dict(api_v2_buffer_goods_task_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



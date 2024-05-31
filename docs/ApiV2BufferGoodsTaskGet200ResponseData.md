# ApiV2BufferGoodsTaskGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **int** | ID загрузки | [optional] 
**buffer_goods** | [**List[GoodBufferHistory]**](GoodBufferHistory.md) | Информация о товарах в загрузке | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_buffer_goods_task_get200_response_data import ApiV2BufferGoodsTaskGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2BufferGoodsTaskGet200ResponseData from a JSON string
api_v2_buffer_goods_task_get200_response_data_instance = ApiV2BufferGoodsTaskGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV2BufferGoodsTaskGet200ResponseData.to_json())

# convert the object into a dict
api_v2_buffer_goods_task_get200_response_data_dict = api_v2_buffer_goods_task_get200_response_data_instance.to_dict()
# create an instance of ApiV2BufferGoodsTaskGet200ResponseData from a dict
api_v2_buffer_goods_task_get200_response_data_from_dict = ApiV2BufferGoodsTaskGet200ResponseData.from_dict(api_v2_buffer_goods_task_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



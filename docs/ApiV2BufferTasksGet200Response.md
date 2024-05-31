# ApiV2BufferTasksGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SupplierTaskMetadataBuffer**](SupplierTaskMetadataBuffer.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_buffer_tasks_get200_response import ApiV2BufferTasksGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2BufferTasksGet200Response from a JSON string
api_v2_buffer_tasks_get200_response_instance = ApiV2BufferTasksGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2BufferTasksGet200Response.to_json())

# convert the object into a dict
api_v2_buffer_tasks_get200_response_dict = api_v2_buffer_tasks_get200_response_instance.to_dict()
# create an instance of ApiV2BufferTasksGet200Response from a dict
api_v2_buffer_tasks_get200_response_from_dict = ApiV2BufferTasksGet200Response.from_dict(api_v2_buffer_tasks_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



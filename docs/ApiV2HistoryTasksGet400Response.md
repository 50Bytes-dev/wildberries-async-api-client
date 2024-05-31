# ApiV2HistoryTasksGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** |  | [optional] 
**error_text** | **str** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_history_tasks_get400_response import ApiV2HistoryTasksGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2HistoryTasksGet400Response from a JSON string
api_v2_history_tasks_get400_response_instance = ApiV2HistoryTasksGet400Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2HistoryTasksGet400Response.to_json())

# convert the object into a dict
api_v2_history_tasks_get400_response_dict = api_v2_history_tasks_get400_response_instance.to_dict()
# create an instance of ApiV2HistoryTasksGet400Response from a dict
api_v2_history_tasks_get400_response_from_dict = ApiV2HistoryTasksGet400Response.from_dict(api_v2_history_tasks_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



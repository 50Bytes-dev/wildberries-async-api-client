# GetTasksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTasksResponseData**](GetTasksResponseData.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.get_tasks_response import GetTasksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTasksResponse from a JSON string
get_tasks_response_instance = GetTasksResponse.from_json(json)
# print the JSON string representation of the object
print(GetTasksResponse.to_json())

# convert the object into a dict
get_tasks_response_dict = get_tasks_response_instance.to_dict()
# create an instance of GetTasksResponse from a dict
get_tasks_response_from_dict = GetTasksResponse.from_dict(get_tasks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



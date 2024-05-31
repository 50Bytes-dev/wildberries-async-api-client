# CreateTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateTaskResponseData**](CreateTaskResponseData.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.create_task_response import CreateTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskResponse from a JSON string
create_task_response_instance = CreateTaskResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTaskResponse.to_json())

# convert the object into a dict
create_task_response_dict = create_task_response_instance.to_dict()
# create an instance of CreateTaskResponse from a dict
create_task_response_from_dict = CreateTaskResponse.from_dict(create_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



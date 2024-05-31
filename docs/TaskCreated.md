# TaskCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskCreatedData**](TaskCreatedData.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.task_created import TaskCreated

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreated from a JSON string
task_created_instance = TaskCreated.from_json(json)
# print the JSON string representation of the object
print(TaskCreated.to_json())

# convert the object into a dict
task_created_dict = task_created_instance.to_dict()
# create an instance of TaskCreated from a dict
task_created_from_dict = TaskCreated.from_dict(task_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



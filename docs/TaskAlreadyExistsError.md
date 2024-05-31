# TaskAlreadyExistsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskAlreadyExistsErrorData**](TaskAlreadyExistsErrorData.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.task_already_exists_error import TaskAlreadyExistsError

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAlreadyExistsError from a JSON string
task_already_exists_error_instance = TaskAlreadyExistsError.from_json(json)
# print the JSON string representation of the object
print(TaskAlreadyExistsError.to_json())

# convert the object into a dict
task_already_exists_error_dict = task_already_exists_error_instance.to_dict()
# create an instance of TaskAlreadyExistsError from a dict
task_already_exists_error_from_dict = TaskAlreadyExistsError.from_dict(task_already_exists_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



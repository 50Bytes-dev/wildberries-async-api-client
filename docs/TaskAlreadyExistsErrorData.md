# TaskAlreadyExistsErrorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID загрузки | [optional] 
**already_exists** | **bool** | Флаг дублирования загрузки: &#x60;true&#x60; — такая загрузка уже есть  | [optional] 

## Example

```python
from wildberries_async_api_client.models.task_already_exists_error_data import TaskAlreadyExistsErrorData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskAlreadyExistsErrorData from a JSON string
task_already_exists_error_data_instance = TaskAlreadyExistsErrorData.from_json(json)
# print the JSON string representation of the object
print(TaskAlreadyExistsErrorData.to_json())

# convert the object into a dict
task_already_exists_error_data_dict = task_already_exists_error_data_instance.to_dict()
# create an instance of TaskAlreadyExistsErrorData from a dict
task_already_exists_error_data_from_dict = TaskAlreadyExistsErrorData.from_dict(task_already_exists_error_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TaskCreatedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID загрузки | [optional] 
**already_exists** | **bool** | Флаг дублирования загрузки: &#x60;true&#x60; — такая загрузка уже есть  | [optional] 

## Example

```python
from wildberries_async_api_client.models.task_created_data import TaskCreatedData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreatedData from a JSON string
task_created_data_instance = TaskCreatedData.from_json(json)
# print the JSON string representation of the object
print(TaskCreatedData.to_json())

# convert the object into a dict
task_created_data_dict = task_created_data_instance.to_dict()
# create an instance of TaskCreatedData from a dict
task_created_data_from_dict = TaskCreatedData.from_dict(task_created_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



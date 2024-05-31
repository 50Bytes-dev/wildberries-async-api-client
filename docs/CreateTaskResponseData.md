# CreateTaskResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | ID задания на генерацию | [optional] 

## Example

```python
from wildberries_async_api_client.models.create_task_response_data import CreateTaskResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaskResponseData from a JSON string
create_task_response_data_instance = CreateTaskResponseData.from_json(json)
# print the JSON string representation of the object
print(CreateTaskResponseData.to_json())

# convert the object into a dict
create_task_response_data_dict = create_task_response_data_instance.to_dict()
# create an instance of CreateTaskResponseData from a dict
create_task_response_data_from_dict = CreateTaskResponseData.from_dict(create_task_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



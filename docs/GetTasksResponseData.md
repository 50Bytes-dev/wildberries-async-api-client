# GetTasksResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID задания | [optional] 
**status** | **str** | Статус задания:      * &#x60;new&#x60; — новое   * &#x60;processing&#x60; —  обрабатывается   * &#x60;done&#x60; — отчёт готов   * &#x60;purged&#x60; — отчёт удалён   * &#x60;canceled&#x60; — отклонено  | [optional] 

## Example

```python
from wildberries_async_api_client.models.get_tasks_response_data import GetTasksResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTasksResponseData from a JSON string
get_tasks_response_data_instance = GetTasksResponseData.from_json(json)
# print the JSON string representation of the object
print(GetTasksResponseData.to_json())

# convert the object into a dict
get_tasks_response_data_dict = get_tasks_response_data_instance.to_dict()
# create an instance of GetTasksResponseData from a dict
get_tasks_response_data_from_dict = GetTasksResponseData.from_dict(get_tasks_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EventsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **int** | Пагинатор. Значение поля необходимо указать в запросе для получения следующего пакета данных. | [optional] 
**newest_event_time** | **str** | Время новейшего события в ответе | [optional] 
**oldest_event_time** | **str** | Время старейшего события в ответе | [optional] 
**total_events** | **int** | Количество событий | [optional] 
**events** | [**List[Event]**](Event.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.events_result import EventsResult

# TODO update the JSON string below
json = "{}"
# create an instance of EventsResult from a JSON string
events_result_instance = EventsResult.from_json(json)
# print the JSON string representation of the object
print(EventsResult.to_json())

# convert the object into a dict
events_result_dict = events_result_instance.to_dict()
# create an instance of EventsResult from a dict
events_result_from_dict = EventsResult.from_dict(events_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



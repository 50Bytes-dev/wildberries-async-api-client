# StatIntervalInterval

Запрошенный временной диапазон.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **date** | Начало запрашиваемого периода | [optional] 
**end** | **date** | Конец запрашиваемого периода | [optional] 

## Example

```python
from wildberries_async_api_client.models.stat_interval_interval import StatIntervalInterval

# TODO update the JSON string below
json = "{}"
# create an instance of StatIntervalInterval from a JSON string
stat_interval_interval_instance = StatIntervalInterval.from_json(json)
# print the JSON string representation of the object
print(StatIntervalInterval.to_json())

# convert the object into a dict
stat_interval_interval_dict = stat_interval_interval_instance.to_dict()
# create an instance of StatIntervalInterval from a dict
stat_interval_interval_from_dict = StatIntervalInterval.from_dict(stat_interval_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



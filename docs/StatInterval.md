# StatInterval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**StatIntervalInterval**](StatIntervalInterval.md) |  | [optional] 
**stats** | [**List[StatsBlok1]**](StatsBlok1.md) | Блок статистики | [optional] 

## Example

```python
from wildberries_async_api_client.models.stat_interval import StatInterval

# TODO update the JSON string below
json = "{}"
# create an instance of StatInterval from a JSON string
stat_interval_instance = StatInterval.from_json(json)
# print the JSON string representation of the object
print(StatInterval.to_json())

# convert the object into a dict
stat_interval_dict = stat_interval_instance.to_dict()
# create an instance of StatInterval from a dict
stat_interval_from_dict = StatInterval.from_dict(stat_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



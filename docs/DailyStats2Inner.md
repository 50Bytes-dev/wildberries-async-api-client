# DailyStats2Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Дата | [optional] 
**app_type_stats** | [**List[DailyStats2InnerAppTypeStatsInner]**](DailyStats2InnerAppTypeStatsInner.md) | Статистика по платформам | [optional] 

## Example

```python
from wildberries_async_api_client.models.daily_stats2_inner import DailyStats2Inner

# TODO update the JSON string below
json = "{}"
# create an instance of DailyStats2Inner from a JSON string
daily_stats2_inner_instance = DailyStats2Inner.from_json(json)
# print the JSON string representation of the object
print(DailyStats2Inner.to_json())

# convert the object into a dict
daily_stats2_inner_dict = daily_stats2_inner_instance.to_dict()
# create an instance of DailyStats2Inner from a dict
daily_stats2_inner_from_dict = DailyStats2Inner.from_dict(daily_stats2_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



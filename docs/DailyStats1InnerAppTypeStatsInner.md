# DailyStats1InnerAppTypeStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип платформы:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - сайт&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;32&lt;/code&gt; - Android&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;64&lt;/code&gt; - IOS&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**stats** | [**List[Stats1Inner]**](Stats1Inner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.daily_stats1_inner_app_type_stats_inner import DailyStats1InnerAppTypeStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DailyStats1InnerAppTypeStatsInner from a JSON string
daily_stats1_inner_app_type_stats_inner_instance = DailyStats1InnerAppTypeStatsInner.from_json(json)
# print the JSON string representation of the object
print(DailyStats1InnerAppTypeStatsInner.to_json())

# convert the object into a dict
daily_stats1_inner_app_type_stats_inner_dict = daily_stats1_inner_app_type_stats_inner_instance.to_dict()
# create an instance of DailyStats1InnerAppTypeStatsInner from a dict
daily_stats1_inner_app_type_stats_inner_from_dict = DailyStats1InnerAppTypeStatsInner.from_dict(daily_stats1_inner_app_type_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



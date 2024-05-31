# AdvV1StatsPost200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**StatIntervalInterval**](StatIntervalInterval.md) |  | [optional] 
**stats** | [**List[StatsBlok1]**](StatsBlok1.md) | Блок статистики | [optional] 
**dates** | **List[date]** | Даты, за которые необходимо выдать информацию. | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_stats_post200_response_inner import AdvV1StatsPost200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1StatsPost200ResponseInner from a JSON string
adv_v1_stats_post200_response_inner_instance = AdvV1StatsPost200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1StatsPost200ResponseInner.to_json())

# convert the object into a dict
adv_v1_stats_post200_response_inner_dict = adv_v1_stats_post200_response_inner_instance.to_dict()
# create an instance of AdvV1StatsPost200ResponseInner from a dict
adv_v1_stats_post200_response_inner_from_dict = AdvV1StatsPost200ResponseInner.from_dict(adv_v1_stats_post200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



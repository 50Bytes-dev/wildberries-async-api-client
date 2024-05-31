# BoosterStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Дата, за которую предоставлены данные. | [optional] 
**nm** | **int** | Артикул WB | [optional] 
**avg_position** | **int** | Средняя позиция товара на страницах поисковой выдачи и каталога | [optional] 

## Example

```python
from wildberries_async_api_client.models.booster_stats_inner import BoosterStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BoosterStatsInner from a JSON string
booster_stats_inner_instance = BoosterStatsInner.from_json(json)
# print the JSON string representation of the object
print(BoosterStatsInner.to_json())

# convert the object into a dict
booster_stats_inner_dict = booster_stats_inner_instance.to_dict()
# create an instance of BoosterStatsInner from a dict
booster_stats_inner_from_dict = BoosterStatsInner.from_dict(booster_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



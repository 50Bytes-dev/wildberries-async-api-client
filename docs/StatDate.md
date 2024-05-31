# StatDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | **List[date]** | Даты, за которые необходимо выдать информацию. | [optional] 
**stats** | [**List[StatsBlok2]**](StatsBlok2.md) | Блок статистики | [optional] 

## Example

```python
from wildberries_async_api_client.models.stat_date import StatDate

# TODO update the JSON string below
json = "{}"
# create an instance of StatDate from a JSON string
stat_date_instance = StatDate.from_json(json)
# print the JSON string representation of the object
print(StatDate.to_json())

# convert the object into a dict
stat_date_dict = stat_date_instance.to_dict()
# create an instance of StatDate from a dict
stat_date_from_dict = StatDate.from_dict(stat_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV2AutoDailyWordsGet200ResponseStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | Ключевая фраза | [optional] 
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **int** | Количество кликов | [optional] 
**ctr** | **float** | Click-Through Rate, отношение количества кликов к количеству показов, % | [optional] 
**sum** | **float** | Затраты, ₽ | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v2_auto_daily_words_get200_response_stat_inner import AdvV2AutoDailyWordsGet200ResponseStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV2AutoDailyWordsGet200ResponseStatInner from a JSON string
adv_v2_auto_daily_words_get200_response_stat_inner_instance = AdvV2AutoDailyWordsGet200ResponseStatInner.from_json(json)
# print the JSON string representation of the object
print(AdvV2AutoDailyWordsGet200ResponseStatInner.to_json())

# convert the object into a dict
adv_v2_auto_daily_words_get200_response_stat_inner_dict = adv_v2_auto_daily_words_get200_response_stat_inner_instance.to_dict()
# create an instance of AdvV2AutoDailyWordsGet200ResponseStatInner from a dict
adv_v2_auto_daily_words_get200_response_stat_inner_from_dict = AdvV2AutoDailyWordsGet200ResponseStatInner.from_dict(adv_v2_auto_daily_words_get200_response_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



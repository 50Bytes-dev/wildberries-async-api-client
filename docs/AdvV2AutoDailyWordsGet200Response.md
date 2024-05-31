# AdvV2AutoDailyWordsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Дата, когда пользователи просматривали товары из кампании | [optional] 
**stat** | [**List[AdvV2AutoDailyWordsGet200ResponseStatInner]**](AdvV2AutoDailyWordsGet200ResponseStatInner.md) | Статистика по ключевым фразам | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v2_auto_daily_words_get200_response import AdvV2AutoDailyWordsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV2AutoDailyWordsGet200Response from a JSON string
adv_v2_auto_daily_words_get200_response_instance = AdvV2AutoDailyWordsGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV2AutoDailyWordsGet200Response.to_json())

# convert the object into a dict
adv_v2_auto_daily_words_get200_response_dict = adv_v2_auto_daily_words_get200_response_instance.to_dict()
# create an instance of AdvV2AutoDailyWordsGet200Response from a dict
adv_v2_auto_daily_words_get200_response_from_dict = AdvV2AutoDailyWordsGet200Response.from_dict(adv_v2_auto_daily_words_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



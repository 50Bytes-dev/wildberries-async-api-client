# AdvV2AutoStatWordsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded** | **List[str]** | Исключения (минус-фразы) для товаров из кампании. Это фразы, которые вы задали с помощью метода Установка/удаление минус-фраз или в личном кабинете, в настройках кампании | [optional] 
**clusters** | [**List[AdvV2AutoStatWordsGet200ResponseClustersInner]**](AdvV2AutoStatWordsGet200ResponseClustersInner.md) | Кластеры ключевых фраз | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v2_auto_stat_words_get200_response import AdvV2AutoStatWordsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV2AutoStatWordsGet200Response from a JSON string
adv_v2_auto_stat_words_get200_response_instance = AdvV2AutoStatWordsGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV2AutoStatWordsGet200Response.to_json())

# convert the object into a dict
adv_v2_auto_stat_words_get200_response_dict = adv_v2_auto_stat_words_get200_response_instance.to_dict()
# create an instance of AdvV2AutoStatWordsGet200Response from a dict
adv_v2_auto_stat_words_get200_response_from_dict = AdvV2AutoStatWordsGet200Response.from_dict(adv_v2_auto_stat_words_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



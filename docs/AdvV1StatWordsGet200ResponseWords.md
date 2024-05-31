# AdvV1StatWordsGet200ResponseWords

Блок информации по ключевым фразам

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phrase** | **List[str]** | Фразовое соответствие (минус фразы) | [optional] 
**strong** | **List[str]** | Точное соответствие (минус фразы) | [optional] 
**excluded** | **List[str]** | Минус фразы из поиска | [optional] 
**pluse** | **List[str]** | Фиксированные фразы | [optional] 
**keywords** | [**List[AdvV1StatWordsGet200ResponseWordsKeywordsInner]**](AdvV1StatWordsGet200ResponseWordsKeywordsInner.md) | Блок со статистикой по ключевым фразам | [optional] 
**fixed** | **bool** | Фиксированные ключевые фразы (&#x60;true&#x60; - включены, &#x60;false&#x60; - выключены)  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_stat_words_get200_response_words import AdvV1StatWordsGet200ResponseWords

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1StatWordsGet200ResponseWords from a JSON string
adv_v1_stat_words_get200_response_words_instance = AdvV1StatWordsGet200ResponseWords.from_json(json)
# print the JSON string representation of the object
print(AdvV1StatWordsGet200ResponseWords.to_json())

# convert the object into a dict
adv_v1_stat_words_get200_response_words_dict = adv_v1_stat_words_get200_response_words_instance.to_dict()
# create an instance of AdvV1StatWordsGet200ResponseWords from a dict
adv_v1_stat_words_get200_response_words_from_dict = AdvV1StatWordsGet200ResponseWords.from_dict(adv_v1_stat_words_get200_response_words_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



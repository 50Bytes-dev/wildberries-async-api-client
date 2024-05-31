# AdvV1StatWordsGet200ResponseStatInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | Идентификатор кампании в системе Wildberries | [optional] 
**keyword** | **str** | Ключевая фраза | [optional] 
**advert_name** | **str** | Поле перманентно отключено | [optional] 
**campaign_name** | **str** | Название кампании | [optional] 
**begin** | **datetime** | Дата запуска кампании | [optional] 
**end** | **datetime** | Дата завершения кампании | [optional] 
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **int** | Количество кликов | [optional] 
**frq** | **int** | Частота (отношение количества просмотров к количеству уникальных пользователей) | [optional] 
**ctr** | **float** | Показатель кликабельности (отношение числа кликов к количеству показов. Выражается в процентах).  | [optional] 
**cpc** | **float** | Стоимость клика, ₽ | [optional] 
**duration** | **int** | Длительность кампании, в секундах | [optional] 
**sum** | **float** | Затраты, ₽. | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_stat_words_get200_response_stat_inner import AdvV1StatWordsGet200ResponseStatInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1StatWordsGet200ResponseStatInner from a JSON string
adv_v1_stat_words_get200_response_stat_inner_instance = AdvV1StatWordsGet200ResponseStatInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1StatWordsGet200ResponseStatInner.to_json())

# convert the object into a dict
adv_v1_stat_words_get200_response_stat_inner_dict = adv_v1_stat_words_get200_response_stat_inner_instance.to_dict()
# create an instance of AdvV1StatWordsGet200ResponseStatInner from a dict
adv_v1_stat_words_get200_response_stat_inner_from_dict = AdvV1StatWordsGet200ResponseStatInner.from_dict(adv_v1_stat_words_get200_response_stat_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



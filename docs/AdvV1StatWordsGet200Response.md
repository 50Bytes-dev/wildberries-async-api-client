# AdvV1StatWordsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**words** | [**AdvV1StatWordsGet200ResponseWords**](AdvV1StatWordsGet200ResponseWords.md) |  | [optional] 
**stat** | [**List[AdvV1StatWordsGet200ResponseStatInner]**](AdvV1StatWordsGet200ResponseStatInner.md) | Массив информации по статистике.&lt;br&gt; &lt;b&gt;Первый элемент массива&lt;/b&gt; с &#x60;keyword: \&quot;Всего по кампании\&quot;&#x60; содержит суммарную информацию по всем ключевым фразам.&lt;br&gt; &lt;b&gt;Каждый следующий элемент массива&lt;/b&gt; содержит информацию по отдельной ключевой фразе.&lt;br&gt; Отображается 60 ключевых фраз с наибольшим количеством просмотров.  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_stat_words_get200_response import AdvV1StatWordsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1StatWordsGet200Response from a JSON string
adv_v1_stat_words_get200_response_instance = AdvV1StatWordsGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV1StatWordsGet200Response.to_json())

# convert the object into a dict
adv_v1_stat_words_get200_response_dict = adv_v1_stat_words_get200_response_instance.to_dict()
# create an instance of AdvV1StatWordsGet200Response from a dict
adv_v1_stat_words_get200_response_from_dict = AdvV1StatWordsGet200Response.from_dict(adv_v1_stat_words_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



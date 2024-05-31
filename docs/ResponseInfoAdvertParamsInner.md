# ResponseInfoAdvertParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_name** | **str** | Название предметной группы (для кампаний в поиске и рекомендациях) | [optional] 
**active** | **bool** | Флаг активности предметной группы, &lt;code&gt;true&lt;/code&gt; - активна, &lt;code&gt;false&lt;/code&gt; - неактивна | [optional] 
**intervals** | [**List[ResponseInfoAdvertParamsInnerIntervalsInner]**](ResponseInfoAdvertParamsInnerIntervalsInner.md) | Интервалы часов показа кампании | [optional] 
**price** | **int** | Текущая ставка | [optional] 
**menu_id** | **int** | Идентификатор меню, где размещается кампания (для кампаний в каталоге) | [optional] 
**subject_id** | **int** | Идентификатор предметной группы, для которой создана кампания (для кампаний в поиске и рекомендациях) | [optional] 
**set_id** | **int** | Идентификатор сочетания предмета и пола (для кампаний в карточке товара) | [optional] 
**set_name** | **str** | Сочетание предмета и пола (для кампаний в карточке товара) | [optional] 
**menu_name** | **str** | Название меню, где размещается кампания (для кампаний в каталоге) | [optional] 
**nms** | [**List[ResponseInfoAdvertParamsInnerNmsInner]**](ResponseInfoAdvertParamsInnerNmsInner.md) | Массив номенклатур кампании | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert_params_inner import ResponseInfoAdvertParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvertParamsInner from a JSON string
response_info_advert_params_inner_instance = ResponseInfoAdvertParamsInner.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvertParamsInner.to_json())

# convert the object into a dict
response_info_advert_params_inner_dict = response_info_advert_params_inner_instance.to_dict()
# create an instance of ResponseInfoAdvertParamsInner from a dict
response_info_advert_params_inner_from_dict = ResponseInfoAdvertParamsInner.from_dict(response_info_advert_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



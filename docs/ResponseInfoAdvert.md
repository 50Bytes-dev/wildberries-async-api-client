# ResponseInfoAdvert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | Идентификатор кампании | [optional] 
**type** | **int** | &lt;dl&gt;   &lt;dt&gt;Тип кампании:&lt;/dt&gt;     &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - кампания  в каталоге&lt;/dd&gt;     &lt;dd&gt;&lt;code&gt;5&lt;/code&gt; - кампания в карточке товара&lt;/dd&gt;     &lt;dd&gt;&lt;code&gt;6&lt;/code&gt; - кампания в поиске&lt;/dd&gt;     &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - кампания в рекомендациях на главной странице&lt;/dd&gt;   &lt;/dl&gt;  | [optional] 
**status** | **int** | &lt;dl&gt; &lt;dt&gt;Статус кампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;-1&lt;/code&gt; - кампания в процессе удаления &lt;/dd&gt; &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - готова к запуску &lt;/dd&gt; &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - Кампания завершена&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; - отказался&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - идут показы&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;11&lt;/code&gt; - Кампания на паузе&lt;/dd&gt; &lt;/dl&gt; Кампания в процессе удаления. Статус означает, что кампания была удалена, и через 3-10 минут она исчезнет из ответа метода.     | [optional] 
**daily_budget** | **int** | Дневной бюджет, если не установлен, то 0 | [optional] 
**create_time** | **str** | Время создания кампании | [optional] 
**change_time** | **str** | Время последнего изменения кампании | [optional] 
**start_time** | **str** | Дата последнего запуска кампании | [optional] 
**end_time** | **str** | Дата завершения кампании | [optional] 
**name** | **str** | Название кампании | [optional] 
**params** | [**List[ResponseInfoAdvertParamsInner]**](ResponseInfoAdvertParamsInner.md) | Параметры кампании | [optional] 
**search_pluse_state** | **bool** | Активность фиксированных фраз (Для кампаний в поиске)  &lt;br&gt; (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены)  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert import ResponseInfoAdvert

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvert from a JSON string
response_info_advert_instance = ResponseInfoAdvert.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvert.to_json())

# convert the object into a dict
response_info_advert_dict = response_info_advert_instance.to_dict()
# create an instance of ResponseInfoAdvert from a dict
response_info_advert_from_dict = ResponseInfoAdvert.from_dict(response_info_advert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



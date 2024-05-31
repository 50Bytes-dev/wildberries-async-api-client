# ResponseInfoAdvertType9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | Идентификатор кампании | [optional] 
**name** | **str** | Название кампании | [optional] 
**type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип кампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - поиск + каталог &lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**status** | **int** | &lt;dl&gt; &lt;dt&gt;Статус кампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;-1&lt;/code&gt; - кампания в процессе удаления &lt;/dd&gt; &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - готова к запуску &lt;/dd&gt; &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - Кампания завершена&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; - отказался&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - идут показы&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;11&lt;/code&gt; - Кампания на паузе&lt;/dd&gt; &lt;/dl&gt; Кампания в процессе удаления. Статус означает, что кампания была удалена, и через 3-10 минут она исчезнет из ответа метода.  | [optional] 
**daily_budget** | **int** | Не используется | [optional] 
**create_time** | **datetime** | Дата создания кампании | [optional] 
**change_time** | **datetime** | Дата последнего изменения кампании | [optional] 
**start_time** | **datetime** | Дата последнего запуска кампании | [optional] 
**end_time** | **datetime** | Дата завершения кампании | [optional] 
**united_params** | [**List[ResponseInfoAdvertType9UnitedParamsInner]**](ResponseInfoAdvertType9UnitedParamsInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert_type9 import ResponseInfoAdvertType9

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvertType9 from a JSON string
response_info_advert_type9_instance = ResponseInfoAdvertType9.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvertType9.to_json())

# convert the object into a dict
response_info_advert_type9_dict = response_info_advert_type9_instance.to_dict()
# create an instance of ResponseInfoAdvertType9 from a dict
response_info_advert_type9_from_dict = ResponseInfoAdvertType9.from_dict(response_info_advert_type9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV1CountGet200ResponseAdverts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип медиакампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - размещение по дням&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;2&lt;/code&gt; - размещение по просмотрам&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**status** | **int** | &lt;dl&gt; &lt;dt&gt;Статус медиакампании:&lt;/dt&gt;   &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - черновик&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;2&lt;/code&gt; - модерация   &lt;dd&gt;&lt;code&gt;3&lt;/code&gt; - отклонено (с возможностью вернуть на модерацию)&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - одобрено&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;5&lt;/code&gt; - запланировано&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;6&lt;/code&gt; - на показах&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - завершено&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; - отказался&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - приостановлена продавцом&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;10&lt;/code&gt; - пауза по дневному лимиту&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;11&lt;/code&gt; - пауза по расходу бюджета&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**count** | **int** | Количество медиакампаний | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_count_get200_response_adverts import AdvV1CountGet200ResponseAdverts

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1CountGet200ResponseAdverts from a JSON string
adv_v1_count_get200_response_adverts_instance = AdvV1CountGet200ResponseAdverts.from_json(json)
# print the JSON string representation of the object
print(AdvV1CountGet200ResponseAdverts.to_json())

# convert the object into a dict
adv_v1_count_get200_response_adverts_dict = adv_v1_count_get200_response_adverts_instance.to_dict()
# create an instance of AdvV1CountGet200ResponseAdverts from a dict
adv_v1_count_get200_response_adverts_from_dict = AdvV1CountGet200ResponseAdverts.from_dict(adv_v1_count_get200_response_adverts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



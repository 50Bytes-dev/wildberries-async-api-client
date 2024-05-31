# AdvV1PromotionAdvertsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | Идентификатор кампании | [optional] 
**type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип кампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - поиск + каталог &lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**status** | **int** | &lt;dl&gt; &lt;dt&gt;Статус кампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;-1&lt;/code&gt; - кампания в процессе удаления &lt;/dd&gt; &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - готова к запуску &lt;/dd&gt; &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - Кампания завершена&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; - отказался&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - идут показы&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;11&lt;/code&gt; - Кампания на паузе&lt;/dd&gt; &lt;/dl&gt; Кампания в процессе удаления. Статус означает, что кампания была удалена, и через 3-10 минут она исчезнет из ответа метода.  | [optional] 
**daily_budget** | **int** | Не используется | [optional] 
**create_time** | **datetime** | Дата создания кампании | [optional] 
**change_time** | **datetime** | Дата последнего изменения кампании | [optional] 
**start_time** | **datetime** | Дата последнего запуска кампании | [optional] 
**end_time** | **datetime** | Дата завершения кампании | [optional] 
**name** | **str** | Название кампании | [optional] 
**params** | [**List[ResponseInfoAdvertParamsInner]**](ResponseInfoAdvertParamsInner.md) | Параметры кампании | [optional] 
**search_pluse_state** | **bool** | Активность фиксированных фраз (Для кампаний в поиске)  &lt;br&gt; (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены)  | [optional] 
**auto_params** | [**ResponseInfoAdvertType8AutoParams**](ResponseInfoAdvertType8AutoParams.md) |  | [optional] 
**united_params** | [**List[ResponseInfoAdvertType9UnitedParamsInner]**](ResponseInfoAdvertType9UnitedParamsInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_promotion_adverts_post200_response import AdvV1PromotionAdvertsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1PromotionAdvertsPost200Response from a JSON string
adv_v1_promotion_adverts_post200_response_instance = AdvV1PromotionAdvertsPost200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV1PromotionAdvertsPost200Response.to_json())

# convert the object into a dict
adv_v1_promotion_adverts_post200_response_dict = adv_v1_promotion_adverts_post200_response_instance.to_dict()
# create an instance of AdvV1PromotionAdvertsPost200Response from a dict
adv_v1_promotion_adverts_post200_response_from_dict = AdvV1PromotionAdvertsPost200Response.from_dict(adv_v1_promotion_adverts_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



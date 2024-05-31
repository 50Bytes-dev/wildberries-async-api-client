# AdvV1UpdGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upd_num** | **int** | Номер выставленного документа (при наличии) | [optional] 
**upd_time** | **str** | Время списания | [optional] 
**upd_sum** | **int** | Выставленная сумма | [optional] 
**advert_id** | **int** | Идентификатор кампании | [optional] 
**camp_name** | **str** | Название кампании | [optional] 
**advert_type** | **int** | Тип кампании | [optional] 
**payment_type** | **str** | &lt;dl&gt; &lt;dt&gt;Источник списания:&lt;/dt&gt; &lt;dd&gt;Баланс&lt;/dd&gt; &lt;dd&gt;Бонусы&lt;/dd&gt; &lt;dd&gt;Счет&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**advert_status** | **int** | &lt;dl&gt;   &lt;dt&gt;Статус кампании:&lt;/dt&gt;   &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - готова к запуску &lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;7&lt;/code&gt; - завершена&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; - отказался&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;9&lt;/code&gt; - активна&lt;/dd&gt;   &lt;dd&gt;&lt;code&gt;11&lt;/code&gt; - приостановлена&lt;/dd&gt; &lt;/dl&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_upd_get200_response_inner import AdvV1UpdGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1UpdGet200ResponseInner from a JSON string
adv_v1_upd_get200_response_inner_instance = AdvV1UpdGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1UpdGet200ResponseInner.to_json())

# convert the object into a dict
adv_v1_upd_get200_response_inner_dict = adv_v1_upd_get200_response_inner_instance.to_dict()
# create an instance of AdvV1UpdGet200ResponseInner from a dict
adv_v1_upd_get200_response_inner_from_dict = AdvV1UpdGet200ResponseInner.from_dict(adv_v1_upd_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



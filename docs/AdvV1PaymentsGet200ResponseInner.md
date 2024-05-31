# AdvV1PaymentsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор платежа | [optional] 
**var_date** | **str** | Дата платежа | [optional] 
**sum** | **int** | Сумма платежа | [optional] 
**type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип источника списания:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;0&lt;/code&gt; - Счёт&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - Баланс&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;3&lt;/code&gt; - Картой&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**status_id** | **int** | &lt;dl&gt; &lt;dt&gt;Статус:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;0&lt;/code&gt; - ошибка&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - обработано&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**card_status** | **str** | &lt;dl&gt; &lt;dt&gt;Статус операции(при оплате картой):&lt;/dt&gt; &lt;dd&gt;&lt;b&gt;success&lt;/b&gt; - успех&lt;/dd&gt; &lt;dd&gt;&lt;b&gt;fail&lt;/b&gt; - неуспех&lt;/dd&gt; &lt;dd&gt;&lt;b&gt;pending&lt;/b&gt; - в ожидании ответа&lt;/dd&gt; &lt;dd&gt;&lt;b&gt;unknown&lt;/b&gt; - неизвестно&lt;/dd&gt; &lt;/dl&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_payments_get200_response_inner import AdvV1PaymentsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1PaymentsGet200ResponseInner from a JSON string
adv_v1_payments_get200_response_inner_instance = AdvV1PaymentsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1PaymentsGet200ResponseInner.to_json())

# convert the object into a dict
adv_v1_payments_get200_response_inner_dict = adv_v1_payments_get200_response_inner_instance.to_dict()
# create an instance of AdvV1PaymentsGet200ResponseInner from a dict
adv_v1_payments_get200_response_inner_from_dict = AdvV1PaymentsGet200ResponseInner.from_dict(adv_v1_payments_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



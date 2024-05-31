# AdvV1BudgetDepositPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **int** | Сумма пополнения (min. 500 ₽) | [optional] 
**type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип источника пополнения:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;0&lt;/code&gt; - Счёт&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - Баланс&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;3&lt;/code&gt; - Бонусы&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**var_return** | **bool** | Флаг возврата ответа (&#x60;true&#x60; - в ответе вернется обновлённый размер бюджета кампании, &#x60;false&#x60; или не указать параметр вообще - не вернётся.) | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_budget_deposit_post_request import AdvV1BudgetDepositPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1BudgetDepositPostRequest from a JSON string
adv_v1_budget_deposit_post_request_instance = AdvV1BudgetDepositPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1BudgetDepositPostRequest.to_json())

# convert the object into a dict
adv_v1_budget_deposit_post_request_dict = adv_v1_budget_deposit_post_request_instance.to_dict()
# create an instance of AdvV1BudgetDepositPostRequest from a dict
adv_v1_budget_deposit_post_request_from_dict = AdvV1BudgetDepositPostRequest.from_dict(adv_v1_budget_deposit_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



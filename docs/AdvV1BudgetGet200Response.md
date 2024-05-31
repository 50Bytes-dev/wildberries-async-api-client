# AdvV1BudgetGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash** | **int** | Поле не используется. Значение всегда 0. | [optional] 
**netting** | **int** | Поле не используется. Значение всегда 0. | [optional] 
**total** | **int** | Бюджет кампании, ₽ | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_budget_get200_response import AdvV1BudgetGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1BudgetGet200Response from a JSON string
adv_v1_budget_get200_response_instance = AdvV1BudgetGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV1BudgetGet200Response.to_json())

# convert the object into a dict
adv_v1_budget_get200_response_dict = adv_v1_budget_get200_response_instance.to_dict()
# create an instance of AdvV1BudgetGet200Response from a dict
adv_v1_budget_get200_response_from_dict = AdvV1BudgetGet200Response.from_dict(adv_v1_budget_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



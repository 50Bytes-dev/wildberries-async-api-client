# Refund

Возврат товара

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**RefundActionType**](RefundActionType.md) |  | [optional] 
**price** | **int** | Стоимость заказа | [optional] 
**price_currency** | **str** | Валюта | [optional] 
**rid** | **str** | Уникальный ID заказа в WB | [optional] 

## Example

```python
from wildberries_async_api_client.models.refund import Refund

# TODO update the JSON string below
json = "{}"
# create an instance of Refund from a JSON string
refund_instance = Refund.from_json(json)
# print the JSON string representation of the object
print(Refund.to_json())

# convert the object into a dict
refund_dict = refund_instance.to_dict()
# create an instance of Refund from a dict
refund_from_dict = Refund.from_dict(refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



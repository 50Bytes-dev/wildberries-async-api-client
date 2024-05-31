# OrderUser

Информация о покупателе (только для доставки силами продавца)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fio** | **str** | ФИО | [optional] 
**phone** | **str** | Номер телефона | [optional] 

## Example

```python
from wildberries_async_api_client.models.order_user import OrderUser

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUser from a JSON string
order_user_instance = OrderUser.from_json(json)
# print the JSON string representation of the object
print(OrderUser.to_json())

# convert the object into a dict
order_user_dict = order_user_instance.to_dict()
# create an instance of OrderUser from a dict
order_user_from_dict = OrderUser.from_dict(order_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



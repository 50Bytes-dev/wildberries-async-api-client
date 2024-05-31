# OrderAddress

Детализованный адрес покупателя для доставки (если применимо). Некоторые из полей могут прийти пустыми из-за специфики адреса

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_address** | **str** | Адрес доставки. | [optional] 
**province** | **str** | Область | [optional] 
**area** | **str** | Район | [optional] 
**city** | **str** | Город | [optional] 
**street** | **str** | Улица | [optional] 
**home** | **str** | Номер дома | [optional] 
**flat** | **str** | Номер квартиры | [optional] 
**entrance** | **str** | Подъезд | [optional] 
**longitude** | **float** | Координата долготы | [optional] 
**latitude** | **float** | Координаты широты | [optional] 

## Example

```python
from wildberries_async_api_client.models.order_address import OrderAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAddress from a JSON string
order_address_instance = OrderAddress.from_json(json)
# print the JSON string representation of the object
print(OrderAddress.to_json())

# convert the object into a dict
order_address_dict = order_address_instance.to_dict()
# create an instance of OrderAddress from a dict
order_address_from_dict = OrderAddress.from_dict(order_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



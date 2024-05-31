# ApiV3SuppliesOrdersReshipmentGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[ApiV3SuppliesOrdersReshipmentGet200ResponseOrdersInner]**](ApiV3SuppliesOrdersReshipmentGet200ResponseOrdersInner.md) | Список заказов | [optional] 

## Example

```python
from wb_client.models.api_v3_supplies_orders_reshipment_get200_response import ApiV3SuppliesOrdersReshipmentGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SuppliesOrdersReshipmentGet200Response from a JSON string
api_v3_supplies_orders_reshipment_get200_response_instance = ApiV3SuppliesOrdersReshipmentGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV3SuppliesOrdersReshipmentGet200Response.to_json())

# convert the object into a dict
api_v3_supplies_orders_reshipment_get200_response_dict = api_v3_supplies_orders_reshipment_get200_response_instance.to_dict()
# create an instance of ApiV3SuppliesOrdersReshipmentGet200Response from a dict
api_v3_supplies_orders_reshipment_get200_response_from_dict = ApiV3SuppliesOrdersReshipmentGet200Response.from_dict(api_v3_supplies_orders_reshipment_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



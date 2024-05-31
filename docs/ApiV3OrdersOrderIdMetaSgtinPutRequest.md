# ApiV3OrdersOrderIdMetaSgtinPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sgtins** | **List[str]** | Массив КиЗов. Допускается от 16 до 135 символов для кода одной маркировки. | [optional] 

## Example

```python
from wb_client.models.api_v3_orders_order_id_meta_sgtin_put_request import ApiV3OrdersOrderIdMetaSgtinPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3OrdersOrderIdMetaSgtinPutRequest from a JSON string
api_v3_orders_order_id_meta_sgtin_put_request_instance = ApiV3OrdersOrderIdMetaSgtinPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3OrdersOrderIdMetaSgtinPutRequest.to_json())

# convert the object into a dict
api_v3_orders_order_id_meta_sgtin_put_request_dict = api_v3_orders_order_id_meta_sgtin_put_request_instance.to_dict()
# create an instance of ApiV3OrdersOrderIdMetaSgtinPutRequest from a dict
api_v3_orders_order_id_meta_sgtin_put_request_from_dict = ApiV3OrdersOrderIdMetaSgtinPutRequest.from_dict(api_v3_orders_order_id_meta_sgtin_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV3StocksWarehouseIdDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skus** | **List[str]** | Массив баркодов | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_stocks_warehouse_id_delete_request import ApiV3StocksWarehouseIdDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3StocksWarehouseIdDeleteRequest from a JSON string
api_v3_stocks_warehouse_id_delete_request_instance = ApiV3StocksWarehouseIdDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3StocksWarehouseIdDeleteRequest.to_json())

# convert the object into a dict
api_v3_stocks_warehouse_id_delete_request_dict = api_v3_stocks_warehouse_id_delete_request_instance.to_dict()
# create an instance of ApiV3StocksWarehouseIdDeleteRequest from a dict
api_v3_stocks_warehouse_id_delete_request_from_dict = ApiV3StocksWarehouseIdDeleteRequest.from_dict(api_v3_stocks_warehouse_id_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



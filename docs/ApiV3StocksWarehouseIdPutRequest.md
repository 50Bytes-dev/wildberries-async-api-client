# ApiV3StocksWarehouseIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks** | [**List[ApiV3StocksWarehouseIdPutRequestStocksInner]**](ApiV3StocksWarehouseIdPutRequestStocksInner.md) | Массив баркодов товаров и их остатков | 

## Example

```python
from wildberries_async_api_client.models.api_v3_stocks_warehouse_id_put_request import ApiV3StocksWarehouseIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3StocksWarehouseIdPutRequest from a JSON string
api_v3_stocks_warehouse_id_put_request_instance = ApiV3StocksWarehouseIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3StocksWarehouseIdPutRequest.to_json())

# convert the object into a dict
api_v3_stocks_warehouse_id_put_request_dict = api_v3_stocks_warehouse_id_put_request_instance.to_dict()
# create an instance of ApiV3StocksWarehouseIdPutRequest from a dict
api_v3_stocks_warehouse_id_put_request_from_dict = ApiV3StocksWarehouseIdPutRequest.from_dict(api_v3_stocks_warehouse_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



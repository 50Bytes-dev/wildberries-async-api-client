# ApiV3StocksWarehouseIdPutRequestStocksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Баркод | [optional] 
**amount** | **int** | Остаток | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_stocks_warehouse_id_put_request_stocks_inner import ApiV3StocksWarehouseIdPutRequestStocksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3StocksWarehouseIdPutRequestStocksInner from a JSON string
api_v3_stocks_warehouse_id_put_request_stocks_inner_instance = ApiV3StocksWarehouseIdPutRequestStocksInner.from_json(json)
# print the JSON string representation of the object
print(ApiV3StocksWarehouseIdPutRequestStocksInner.to_json())

# convert the object into a dict
api_v3_stocks_warehouse_id_put_request_stocks_inner_dict = api_v3_stocks_warehouse_id_put_request_stocks_inner_instance.to_dict()
# create an instance of ApiV3StocksWarehouseIdPutRequestStocksInner from a dict
api_v3_stocks_warehouse_id_put_request_stocks_inner_from_dict = ApiV3StocksWarehouseIdPutRequestStocksInner.from_dict(api_v3_stocks_warehouse_id_put_request_stocks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



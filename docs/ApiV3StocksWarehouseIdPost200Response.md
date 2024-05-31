# ApiV3StocksWarehouseIdPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks** | [**List[ApiV3StocksWarehouseIdPost200ResponseStocksInner]**](ApiV3StocksWarehouseIdPost200ResponseStocksInner.md) |  | [optional] 

## Example

```python
from wb_client.models.api_v3_stocks_warehouse_id_post200_response import ApiV3StocksWarehouseIdPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3StocksWarehouseIdPost200Response from a JSON string
api_v3_stocks_warehouse_id_post200_response_instance = ApiV3StocksWarehouseIdPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV3StocksWarehouseIdPost200Response.to_json())

# convert the object into a dict
api_v3_stocks_warehouse_id_post200_response_dict = api_v3_stocks_warehouse_id_post200_response_instance.to_dict()
# create an instance of ApiV3StocksWarehouseIdPost200Response from a dict
api_v3_stocks_warehouse_id_post200_response_from_dict = ApiV3StocksWarehouseIdPost200Response.from_dict(api_v3_stocks_warehouse_id_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



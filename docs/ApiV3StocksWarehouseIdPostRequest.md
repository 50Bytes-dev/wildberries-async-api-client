# ApiV3StocksWarehouseIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skus** | **List[str]** | Массив баркодов | [optional] 

## Example

```python
from wb_client.models.api_v3_stocks_warehouse_id_post_request import ApiV3StocksWarehouseIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3StocksWarehouseIdPostRequest from a JSON string
api_v3_stocks_warehouse_id_post_request_instance = ApiV3StocksWarehouseIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3StocksWarehouseIdPostRequest.to_json())

# convert the object into a dict
api_v3_stocks_warehouse_id_post_request_dict = api_v3_stocks_warehouse_id_post_request_instance.to_dict()
# create an instance of ApiV3StocksWarehouseIdPostRequest from a dict
api_v3_stocks_warehouse_id_post_request_from_dict = ApiV3StocksWarehouseIdPostRequest.from_dict(api_v3_stocks_warehouse_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



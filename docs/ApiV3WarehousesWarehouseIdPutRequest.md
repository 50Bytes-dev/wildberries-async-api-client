# ApiV3WarehousesWarehouseIdPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Имя склада продавца | 
**office_id** | **int** | Идентификатор склада WB | 

## Example

```python
from wildberries_async_api_client.models.api_v3_warehouses_warehouse_id_put_request import ApiV3WarehousesWarehouseIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3WarehousesWarehouseIdPutRequest from a JSON string
api_v3_warehouses_warehouse_id_put_request_instance = ApiV3WarehousesWarehouseIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3WarehousesWarehouseIdPutRequest.to_json())

# convert the object into a dict
api_v3_warehouses_warehouse_id_put_request_dict = api_v3_warehouses_warehouse_id_put_request_instance.to_dict()
# create an instance of ApiV3WarehousesWarehouseIdPutRequest from a dict
api_v3_warehouses_warehouse_id_put_request_from_dict = ApiV3WarehousesWarehouseIdPutRequest.from_dict(api_v3_warehouses_warehouse_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



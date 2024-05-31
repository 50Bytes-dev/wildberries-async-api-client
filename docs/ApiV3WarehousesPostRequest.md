# ApiV3WarehousesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Имя склада продавца | 
**office_id** | **int** | ID склада WB | 

## Example

```python
from wb_client.models.api_v3_warehouses_post_request import ApiV3WarehousesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3WarehousesPostRequest from a JSON string
api_v3_warehouses_post_request_instance = ApiV3WarehousesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3WarehousesPostRequest.to_json())

# convert the object into a dict
api_v3_warehouses_post_request_dict = api_v3_warehouses_post_request_instance.to_dict()
# create an instance of ApiV3WarehousesPostRequest from a dict
api_v3_warehouses_post_request_from_dict = ApiV3WarehousesPostRequest.from_dict(api_v3_warehouses_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



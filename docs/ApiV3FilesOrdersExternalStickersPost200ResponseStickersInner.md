# ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Идентификатор сборочного задания | [optional] 
**url** | **str** | Ссылка, по которой можно получить этикетку для сборочного задания | [optional] 
**parcel_id** | **str** | Трек-номер в этикетке для отслеживания сборочного задания | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_files_orders_external_stickers_post200_response_stickers_inner import ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner from a JSON string
api_v3_files_orders_external_stickers_post200_response_stickers_inner_instance = ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner.from_json(json)
# print the JSON string representation of the object
print(ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner.to_json())

# convert the object into a dict
api_v3_files_orders_external_stickers_post200_response_stickers_inner_dict = api_v3_files_orders_external_stickers_post200_response_stickers_inner_instance.to_dict()
# create an instance of ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner from a dict
api_v3_files_orders_external_stickers_post200_response_stickers_inner_from_dict = ApiV3FilesOrdersExternalStickersPost200ResponseStickersInner.from_dict(api_v3_files_orders_external_stickers_post200_response_stickers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



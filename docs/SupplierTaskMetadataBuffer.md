# SupplierTaskMetadataBuffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **int** | ID загрузки | [optional] 
**status** | **int** | Статус загрузки: &#x60;1&#x60; — в обработке  | [optional] 
**upload_date** | **date** | Дата и время, когда загрузка создана | [optional] 
**activation_date** | **date** | Дата и время, когда загрузка отправляется в обработку | [optional] 
**over_all_goods_number** | **int** | Всего товаров | [optional] 
**success_goods_number** | **int** | Товаров без ошибок (0, потому что загрузка в обработке) | [optional] 

## Example

```python
from wildberries_async_api_client.models.supplier_task_metadata_buffer import SupplierTaskMetadataBuffer

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierTaskMetadataBuffer from a JSON string
supplier_task_metadata_buffer_instance = SupplierTaskMetadataBuffer.from_json(json)
# print the JSON string representation of the object
print(SupplierTaskMetadataBuffer.to_json())

# convert the object into a dict
supplier_task_metadata_buffer_dict = supplier_task_metadata_buffer_instance.to_dict()
# create an instance of SupplierTaskMetadataBuffer from a dict
supplier_task_metadata_buffer_from_dict = SupplierTaskMetadataBuffer.from_dict(supplier_task_metadata_buffer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



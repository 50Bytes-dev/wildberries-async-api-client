# ModelsWarehousesResultItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID склада | [optional] 
**name** | **str** | Название склада | [optional] 
**address** | **str** | Адрес склада | [optional] 
**work_time** | **str** | Режим работы склада | [optional] 
**accepts_qr** | **bool** | Принимает ли склад QR-поставки: - &#x60;true&#x60; — да - &#x60;false&#x60; — нет  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_warehouses_result_items import ModelsWarehousesResultItems

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWarehousesResultItems from a JSON string
models_warehouses_result_items_instance = ModelsWarehousesResultItems.from_json(json)
# print the JSON string representation of the object
print(ModelsWarehousesResultItems.to_json())

# convert the object into a dict
models_warehouses_result_items_dict = models_warehouses_result_items_instance.to_dict()
# create an instance of ModelsWarehousesResultItems from a dict
models_warehouses_result_items_from_dict = ModelsWarehousesResultItems.from_dict(models_warehouses_result_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



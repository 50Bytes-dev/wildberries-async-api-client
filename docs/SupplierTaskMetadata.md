# SupplierTaskMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **int** | ID загрузки | [optional] 
**status** | **int** | Статус загрузки:    * &#x60;3&#x60; — обработана, в товарах нет ошибок, цены и скидки обновились   * &#x60;4&#x60; — отменена   * &#x60;5&#x60; — обработана, но в товарах есть ошибки. Для товаров без ошибок цены и скидки обновились, а ошибки в остальных товарах можно получить с помощью метода [Детализация обработанной загрузки](#tag/Istoriya-zagruzok/paths/~1api~1v2~1history~1goods~1task/get)   * &#x60;6&#x60; — обработана, но во всех товарах есть ошибки. Их тоже можно получить с помощью метода [Детализация обработанной загрузки](#tag/Istoriya-zagruzok/paths/~1api~1v2~1history~1goods~1task/get)  | [optional] 
**upload_date** | **date** | Дата и время, когда загрузка создана | [optional] 
**activation_date** | **date** | Дата и время, когда загрузка отправляется в обработку | [optional] 
**over_all_goods_number** | **int** | Всего товаров | [optional] 
**success_goods_number** | **int** | Товаров без ошибок | [optional] 

## Example

```python
from wildberries_async_api_client.models.supplier_task_metadata import SupplierTaskMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierTaskMetadata from a JSON string
supplier_task_metadata_instance = SupplierTaskMetadata.from_json(json)
# print the JSON string representation of the object
print(SupplierTaskMetadata.to_json())

# convert the object into a dict
supplier_task_metadata_dict = supplier_task_metadata_instance.to_dict()
# create an instance of SupplierTaskMetadata from a dict
supplier_task_metadata_from_dict = SupplierTaskMetadata.from_dict(supplier_task_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



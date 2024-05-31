# ModelsWarehouseBoxRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_delivery_and_storage_expr** | **str** | Коэффициент, %. На него умножается стоимость доставки и хранения. Во всех тарифах этот коэффициент уже учтён | [optional] 
**box_delivery_base** | **str** | Доставка 1 литра, ₽ | [optional] 
**box_delivery_liter** | **str** | Доставка каждого дополнительного литра, ₽ | [optional] 
**box_storage_base** | **str** | Хранение 1 литра, ₽ | [optional] 
**box_storage_liter** | **str** | Хранение каждого дополнительного литра, ₽ | [optional] 
**warehouse_name** | **str** | Название склада | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_warehouse_box_rates import ModelsWarehouseBoxRates

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWarehouseBoxRates from a JSON string
models_warehouse_box_rates_instance = ModelsWarehouseBoxRates.from_json(json)
# print the JSON string representation of the object
print(ModelsWarehouseBoxRates.to_json())

# convert the object into a dict
models_warehouse_box_rates_dict = models_warehouse_box_rates_instance.to_dict()
# create an instance of ModelsWarehouseBoxRates from a dict
models_warehouse_box_rates_from_dict = ModelsWarehouseBoxRates.from_dict(models_warehouse_box_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



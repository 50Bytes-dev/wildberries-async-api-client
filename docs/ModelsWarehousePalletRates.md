# ModelsWarehousePalletRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pallet_delivery_expr** | **str** | Коэффициент доставки, %. На него умножается стоимость доставки. Во всех тарифах этот коэффициент уже учтён | [optional] 
**pallet_delivery_value_base** | **str** | Доставка 1 литра, ₽ | [optional] 
**pallet_delivery_value_liter** | **str** | Доставка каждого дополнительного литра, ₽ | [optional] 
**pallet_storage_expr** | **str** | Коэффициент хранения, %. На него умножается стоимость хранения. Во всех тарифах этот коэффициент уже учтён | [optional] 
**pallet_storage_value_expr** | **str** | Хранение 1 монопаллеты, ₽ | [optional] 
**warehouse_name** | **str** | Название склада | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_warehouse_pallet_rates import ModelsWarehousePalletRates

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWarehousePalletRates from a JSON string
models_warehouse_pallet_rates_instance = ModelsWarehousePalletRates.from_json(json)
# print the JSON string representation of the object
print(ModelsWarehousePalletRates.to_json())

# convert the object into a dict
models_warehouse_pallet_rates_dict = models_warehouse_pallet_rates_instance.to_dict()
# create an instance of ModelsWarehousePalletRates from a dict
models_warehouse_pallet_rates_from_dict = ModelsWarehousePalletRates.from_dict(models_warehouse_pallet_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



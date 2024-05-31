# ModelsWarehousesPalletRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_from_min** | **str** | Дата начала тарифа | [optional] 
**dt_next_pallet** | **str** | Дата начала следующего тарифа | [optional] 
**dt_till_max** | **str** | Дата окончания тарифа | [optional] 
**warehouse_list** | [**List[ModelsWarehousePalletRates]**](ModelsWarehousePalletRates.md) | Тарифы для монопаллет, сгруппированные по складам | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_warehouses_pallet_rates import ModelsWarehousesPalletRates

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWarehousesPalletRates from a JSON string
models_warehouses_pallet_rates_instance = ModelsWarehousesPalletRates.from_json(json)
# print the JSON string representation of the object
print(ModelsWarehousesPalletRates.to_json())

# convert the object into a dict
models_warehouses_pallet_rates_dict = models_warehouses_pallet_rates_instance.to_dict()
# create an instance of ModelsWarehousesPalletRates from a dict
models_warehouses_pallet_rates_from_dict = ModelsWarehousesPalletRates.from_dict(models_warehouses_pallet_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



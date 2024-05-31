# ModelsWarehousesBoxRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_from_min** | **str** | Дата начала тарифа | [optional] 
**dt_next_box** | **str** | Дата начала следующего тарифа | [optional] 
**dt_till_max** | **str** | Дата окончания тарифа | [optional] 
**warehouse_list** | [**List[ModelsWarehouseBoxRates]**](ModelsWarehouseBoxRates.md) | Тарифы для коробов, сгруппированные по складам | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_warehouses_box_rates import ModelsWarehousesBoxRates

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWarehousesBoxRates from a JSON string
models_warehouses_box_rates_instance = ModelsWarehousesBoxRates.from_json(json)
# print the JSON string representation of the object
print(ModelsWarehousesBoxRates.to_json())

# convert the object into a dict
models_warehouses_box_rates_dict = models_warehouses_box_rates_instance.to_dict()
# create an instance of ModelsWarehousesBoxRates from a dict
models_warehouses_box_rates_from_dict = ModelsWarehousesBoxRates.from_dict(models_warehouses_box_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



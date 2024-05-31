# ModelsWarehousesReturnRates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_next_delivery_dump_kgt** | **str** | Дата начала следующего тарифа при грузовой доставке | [optional] 
**dt_next_delivery_dump_srg** | **str** | Дата начала следующего тарифа для неопознанных товаров | [optional] 
**dt_next_delivery_dump_sup** | **str** | Дата начала следующего тарифа при обычной доставке | [optional] 
**warehouse_list** | [**List[ModelsWarehouseReturnRates]**](ModelsWarehouseReturnRates.md) | &lt;p&gt;Тарифы на возврат, сгруппированные по складам:&lt;/p&gt; &lt;ul&gt;   &lt;li&gt;стоимость возврата брака и возврата по инициативе продавца при грузовой доставке;&lt;/li&gt;   &lt;li&gt;стоимость возврата неопознанного складом товара;&lt;/li&gt;   &lt;li&gt;стоимость возврата брака и возврата по инициативе продавца (в пункт выдачи и обратно).&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Можно получить стоимость возврата в пункт выдачи (ПВЗ) и обратной логистики — если продавец не забрал товары из пункта выдачи за 7 дней.&lt;/p&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_warehouses_return_rates import ModelsWarehousesReturnRates

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsWarehousesReturnRates from a JSON string
models_warehouses_return_rates_instance = ModelsWarehousesReturnRates.from_json(json)
# print the JSON string representation of the object
print(ModelsWarehousesReturnRates.to_json())

# convert the object into a dict
models_warehouses_return_rates_dict = models_warehouses_return_rates_instance.to_dict()
# create an instance of ModelsWarehousesReturnRates from a dict
models_warehouses_return_rates_from_dict = ModelsWarehousesReturnRates.from_dict(models_warehouses_return_rates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelsOptionsResultModelResultInnerWarehousesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouse_id** | **int** | ID склада. По нему можно получить [информацию о складе](./#tag/Informaciya-dlya-formirovaniya-postavok/paths/~1api~1v1~1warehouses/get) | [optional] 
**can_box** | **bool** | Тип упаковки **Короб**:   - &#x60;true&#x60; — доступен   - &#x60;false&#x60; — недоступен  | [optional] 
**can_monopallet** | **bool** | Тип упаковки **Монопаллета**:   - &#x60;true&#x60; — доступен   - &#x60;false&#x60; — недоступен  | [optional] 
**can_supersafe** | **bool** | Тип упаковки **Суперсейф**:   - &#x60;true&#x60; — доступен   - &#x60;false&#x60; — недоступен  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_options_result_model_result_inner_warehouses_inner import ModelsOptionsResultModelResultInnerWarehousesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsOptionsResultModelResultInnerWarehousesInner from a JSON string
models_options_result_model_result_inner_warehouses_inner_instance = ModelsOptionsResultModelResultInnerWarehousesInner.from_json(json)
# print the JSON string representation of the object
print(ModelsOptionsResultModelResultInnerWarehousesInner.to_json())

# convert the object into a dict
models_options_result_model_result_inner_warehouses_inner_dict = models_options_result_model_result_inner_warehouses_inner_instance.to_dict()
# create an instance of ModelsOptionsResultModelResultInnerWarehousesInner from a dict
models_options_result_model_result_inner_warehouses_inner_from_dict = ModelsOptionsResultModelResultInnerWarehousesInner.from_dict(models_options_result_model_result_inner_warehouses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



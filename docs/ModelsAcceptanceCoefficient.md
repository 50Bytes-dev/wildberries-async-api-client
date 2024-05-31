# ModelsAcceptanceCoefficient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Дата начала действия коэффициента | [optional] 
**coefficient** | **float** | Коэффициент приёмки:   - &#x60;-1&#x60; — поставка недоступна   - &#x60;0&#x60; — бесплатная поставка   - от &#x60;1&#x60; — множитель стоимости приёмки  | [optional] 
**warehouse_id** | **int** | ID склада. По нему можно получить [информацию о складе](./#tag/Informaciya-dlya-formirovaniya-postavok/paths/~1api~1v1~1warehouses/get) | [optional] 
**warehouse_name** | **str** | Название склада | [optional] 
**box_type_name** | **str** | Тип поставки:   - &#x60;Короба&#x60;   - &#x60;Монопаллеты&#x60;   - &#x60;Суперсейф&#x60;   - &#x60;QR-поставка с коробами&#x60;  | [optional] 
**box_type_id** | **int** | ID типа поставки:   - &#x60;2&#x60; — Короба   - &#x60;5&#x60; — Монопаллеты   - &#x60;6&#x60; — Суперсейф &lt;br&gt;Для типа поставки **QR-поставка с коробами** поле не возвращается  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_acceptance_coefficient import ModelsAcceptanceCoefficient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsAcceptanceCoefficient from a JSON string
models_acceptance_coefficient_instance = ModelsAcceptanceCoefficient.from_json(json)
# print the JSON string representation of the object
print(ModelsAcceptanceCoefficient.to_json())

# convert the object into a dict
models_acceptance_coefficient_dict = models_acceptance_coefficient_instance.to_dict()
# create an instance of ModelsAcceptanceCoefficient from a dict
models_acceptance_coefficient_from_dict = ModelsAcceptanceCoefficient.from_dict(models_acceptance_coefficient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelsOptionsResultModelResultInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Баркод из карточки товара | [optional] 
**error** | [**ModelsOptionsResultModelResultInnerError**](ModelsOptionsResultModelResultInnerError.md) |  | [optional] 
**is_error** | **bool** | Наличие ошибки:   - &#x60;true&#x60; — ошибка есть   - Поля нет — ошибка отсутствует     | [optional] 
**warehouses** | [**List[ModelsOptionsResultModelResultInnerWarehousesInner]**](ModelsOptionsResultModelResultInnerWarehousesInner.md) | Список складов. При наличии ошибки будет &#x60;null&#x60; | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_options_result_model_result_inner import ModelsOptionsResultModelResultInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsOptionsResultModelResultInner from a JSON string
models_options_result_model_result_inner_instance = ModelsOptionsResultModelResultInner.from_json(json)
# print the JSON string representation of the object
print(ModelsOptionsResultModelResultInner.to_json())

# convert the object into a dict
models_options_result_model_result_inner_dict = models_options_result_model_result_inner_instance.to_dict()
# create an instance of ModelsOptionsResultModelResultInner from a dict
models_options_result_model_result_inner_from_dict = ModelsOptionsResultModelResultInner.from_dict(models_options_result_model_result_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



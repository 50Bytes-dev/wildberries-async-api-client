# ModelsReturnTariffsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsWarehousesReturnRates**](ModelsWarehousesReturnRates.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_return_tariffs_response import ModelsReturnTariffsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsReturnTariffsResponse from a JSON string
models_return_tariffs_response_instance = ModelsReturnTariffsResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsReturnTariffsResponse.to_json())

# convert the object into a dict
models_return_tariffs_response_dict = models_return_tariffs_response_instance.to_dict()
# create an instance of ModelsReturnTariffsResponse from a dict
models_return_tariffs_response_from_dict = ModelsReturnTariffsResponse.from_dict(models_return_tariffs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



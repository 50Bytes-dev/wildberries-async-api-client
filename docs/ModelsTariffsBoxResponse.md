# ModelsTariffsBoxResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsWarehousesBoxRates**](ModelsWarehousesBoxRates.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_tariffs_box_response import ModelsTariffsBoxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsTariffsBoxResponse from a JSON string
models_tariffs_box_response_instance = ModelsTariffsBoxResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsTariffsBoxResponse.to_json())

# convert the object into a dict
models_tariffs_box_response_dict = models_tariffs_box_response_instance.to_dict()
# create an instance of ModelsTariffsBoxResponse from a dict
models_tariffs_box_response_from_dict = ModelsTariffsBoxResponse.from_dict(models_tariffs_box_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelsTariffsPalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ModelsWarehousesPalletRates**](ModelsWarehousesPalletRates.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_tariffs_pallet_response import ModelsTariffsPalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsTariffsPalletResponse from a JSON string
models_tariffs_pallet_response_instance = ModelsTariffsPalletResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsTariffsPalletResponse.to_json())

# convert the object into a dict
models_tariffs_pallet_response_dict = models_tariffs_pallet_response_instance.to_dict()
# create an instance of ModelsTariffsPalletResponse from a dict
models_tariffs_pallet_response_from_dict = ModelsTariffsPalletResponse.from_dict(models_tariffs_pallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



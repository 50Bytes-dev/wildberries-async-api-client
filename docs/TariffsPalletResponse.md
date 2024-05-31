# TariffsPalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ModelsTariffsPalletResponse**](ModelsTariffsPalletResponse.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.tariffs_pallet_response import TariffsPalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TariffsPalletResponse from a JSON string
tariffs_pallet_response_instance = TariffsPalletResponse.from_json(json)
# print the JSON string representation of the object
print(TariffsPalletResponse.to_json())

# convert the object into a dict
tariffs_pallet_response_dict = tariffs_pallet_response_instance.to_dict()
# create an instance of TariffsPalletResponse from a dict
tariffs_pallet_response_from_dict = TariffsPalletResponse.from_dict(tariffs_pallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TariffsBoxResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ModelsTariffsBoxResponse**](ModelsTariffsBoxResponse.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.tariffs_box_response import TariffsBoxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TariffsBoxResponse from a JSON string
tariffs_box_response_instance = TariffsBoxResponse.from_json(json)
# print the JSON string representation of the object
print(TariffsBoxResponse.to_json())

# convert the object into a dict
tariffs_box_response_dict = tariffs_box_response_instance.to_dict()
# create an instance of TariffsBoxResponse from a dict
tariffs_box_response_from_dict = TariffsBoxResponse.from_dict(tariffs_box_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



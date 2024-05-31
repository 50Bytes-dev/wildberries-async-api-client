# ReturnTariffsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ModelsReturnTariffsResponse**](ModelsReturnTariffsResponse.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.return_tariffs_response import ReturnTariffsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnTariffsResponse from a JSON string
return_tariffs_response_instance = ReturnTariffsResponse.from_json(json)
# print the JSON string representation of the object
print(ReturnTariffsResponse.to_json())

# convert the object into a dict
return_tariffs_response_dict = return_tariffs_response_instance.to_dict()
# create an instance of ReturnTariffsResponse from a dict
return_tariffs_response_from_dict = ReturnTariffsResponse.from_dict(return_tariffs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ErrorInternalResponse

Прочие ошибки

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**error_text** | **str** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.error_internal_response import ErrorInternalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorInternalResponse from a JSON string
error_internal_response_instance = ErrorInternalResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorInternalResponse.to_json())

# convert the object into a dict
error_internal_response_dict = error_internal_response_instance.to_dict()
# create an instance of ErrorInternalResponse from a dict
error_internal_response_from_dict = ErrorInternalResponse.from_dict(error_internal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



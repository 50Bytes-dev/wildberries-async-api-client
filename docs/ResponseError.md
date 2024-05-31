# ResponseError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_error import ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseError from a JSON string
response_error_instance = ResponseError.from_json(json)
# print the JSON string representation of the object
print(ResponseError.to_json())

# convert the object into a dict
response_error_dict = response_error_instance.to_dict()
# create an instance of ResponseError from a dict
response_error_from_dict = ResponseError.from_dict(response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



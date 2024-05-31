# ResponseErrorAdditionalErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Структура, где допущена ошибка | [optional] 
**description** | **str** | Описание | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_error_additional_errors_inner import ResponseErrorAdditionalErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseErrorAdditionalErrorsInner from a JSON string
response_error_additional_errors_inner_instance = ResponseErrorAdditionalErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ResponseErrorAdditionalErrorsInner.to_json())

# convert the object into a dict
response_error_additional_errors_inner_dict = response_error_additional_errors_inner_instance.to_dict()
# create an instance of ResponseErrorAdditionalErrorsInner from a dict
response_error_additional_errors_inner_from_dict = ResponseErrorAdditionalErrorsInner.from_dict(response_error_additional_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ResponseContentError4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**ResponseContentError4AdditionalErrors**](ResponseContentError4AdditionalErrors.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_content_error4 import ResponseContentError4

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseContentError4 from a JSON string
response_content_error4_instance = ResponseContentError4.from_json(json)
# print the JSON string representation of the object
print(ResponseContentError4.to_json())

# convert the object into a dict
response_content_error4_dict = response_content_error4_instance.to_dict()
# create an instance of ResponseContentError4 from a dict
response_content_error4_from_dict = ResponseContentError4.from_dict(response_content_error4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



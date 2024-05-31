# ResponseBodyContentError400


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**ResponseBodyContentError400AdditionalErrors**](ResponseBodyContentError400AdditionalErrors.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_body_content_error400 import ResponseBodyContentError400

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBodyContentError400 from a JSON string
response_body_content_error400_instance = ResponseBodyContentError400.from_json(json)
# print the JSON string representation of the object
print(ResponseBodyContentError400.to_json())

# convert the object into a dict
response_body_content_error400_dict = response_body_content_error400_instance.to_dict()
# create an instance of ResponseBodyContentError400 from a dict
response_body_content_error400_from_dict = ResponseBodyContentError400.from_dict(response_body_content_error400_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



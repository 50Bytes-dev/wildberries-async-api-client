# ResponseContentError1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**ResponseContentError1AdditionalErrors**](ResponseContentError1AdditionalErrors.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_content_error1 import ResponseContentError1

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseContentError1 from a JSON string
response_content_error1_instance = ResponseContentError1.from_json(json)
# print the JSON string representation of the object
print(ResponseContentError1.to_json())

# convert the object into a dict
response_content_error1_dict = response_content_error1_instance.to_dict()
# create an instance of ResponseContentError1 from a dict
response_content_error1_from_dict = ResponseContentError1.from_dict(response_content_error1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ResponseContentError5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**ResponseContentError5AdditionalErrors**](ResponseContentError5AdditionalErrors.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_content_error5 import ResponseContentError5

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseContentError5 from a JSON string
response_content_error5_instance = ResponseContentError5.from_json(json)
# print the JSON string representation of the object
print(ResponseContentError5.to_json())

# convert the object into a dict
response_content_error5_dict = response_content_error5_instance.to_dict()
# create an instance of ResponseContentError5 from a dict
response_content_error5_from_dict = ResponseContentError5.from_dict(response_content_error5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



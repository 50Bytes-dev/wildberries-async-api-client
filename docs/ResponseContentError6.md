# ResponseContentError6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **str** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_content_error6 import ResponseContentError6

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseContentError6 from a JSON string
response_content_error6_instance = ResponseContentError6.from_json(json)
# print the JSON string representation of the object
print(ResponseContentError6.to_json())

# convert the object into a dict
response_content_error6_dict = response_content_error6_instance.to_dict()
# create an instance of ResponseContentError6 from a dict
response_content_error6_from_dict = ResponseContentError6.from_dict(response_content_error6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



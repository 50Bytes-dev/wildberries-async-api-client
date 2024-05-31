# ResponseBodyContentError403


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **str** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_body_content_error403 import ResponseBodyContentError403

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBodyContentError403 from a JSON string
response_body_content_error403_instance = ResponseBodyContentError403.from_json(json)
# print the JSON string representation of the object
print(ResponseBodyContentError403.to_json())

# convert the object into a dict
response_body_content_error403_dict = response_body_content_error403_instance.to_dict()
# create an instance of ResponseBodyContentError403 from a dict
response_body_content_error403_from_dict = ResponseBodyContentError403.from_dict(response_body_content_error403_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



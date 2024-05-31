# ResponseErrorTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_error_template import ResponseErrorTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseErrorTemplate from a JSON string
response_error_template_instance = ResponseErrorTemplate.from_json(json)
# print the JSON string representation of the object
print(ResponseErrorTemplate.to_json())

# convert the object into a dict
response_error_template_dict = response_error_template_instance.to_dict()
# create an instance of ResponseErrorTemplate from a dict
response_error_template_from_dict = ResponseErrorTemplate.from_dict(response_error_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



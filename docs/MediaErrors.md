# MediaErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_errors** | **object** | Дополнительные ошибки | [optional] 
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.media_errors import MediaErrors

# TODO update the JSON string below
json = "{}"
# create an instance of MediaErrors from a JSON string
media_errors_instance = MediaErrors.from_json(json)
# print the JSON string representation of the object
print(MediaErrors.to_json())

# convert the object into a dict
media_errors_dict = media_errors_instance.to_dict()
# create an instance of MediaErrors from a dict
media_errors_from_dict = MediaErrors.from_dict(media_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



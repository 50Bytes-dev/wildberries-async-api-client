# ContentV3MediaSavePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **object** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v3_media_save_post200_response import ContentV3MediaSavePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV3MediaSavePost200Response from a JSON string
content_v3_media_save_post200_response_instance = ContentV3MediaSavePost200Response.from_json(json)
# print the JSON string representation of the object
print(ContentV3MediaSavePost200Response.to_json())

# convert the object into a dict
content_v3_media_save_post200_response_dict = content_v3_media_save_post200_response_instance.to_dict()
# create an instance of ContentV3MediaSavePost200Response from a dict
content_v3_media_save_post200_response_from_dict = ContentV3MediaSavePost200Response.from_dict(content_v3_media_save_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



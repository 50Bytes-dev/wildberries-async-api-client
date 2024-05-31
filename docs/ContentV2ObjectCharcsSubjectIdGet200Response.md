# ContentV2ObjectCharcsSubjectIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner]**](ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner.md) | Данные | [optional] 
**error** | **bool** | Флаг наличия ошибки | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 
**additional_errors** | **str** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_object_charcs_subject_id_get200_response import ContentV2ObjectCharcsSubjectIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2ObjectCharcsSubjectIdGet200Response from a JSON string
content_v2_object_charcs_subject_id_get200_response_instance = ContentV2ObjectCharcsSubjectIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(ContentV2ObjectCharcsSubjectIdGet200Response.to_json())

# convert the object into a dict
content_v2_object_charcs_subject_id_get200_response_dict = content_v2_object_charcs_subject_id_get200_response_instance.to_dict()
# create an instance of ContentV2ObjectCharcsSubjectIdGet200Response from a dict
content_v2_object_charcs_subject_id_get200_response_from_dict = ContentV2ObjectCharcsSubjectIdGet200Response.from_dict(content_v2_object_charcs_subject_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



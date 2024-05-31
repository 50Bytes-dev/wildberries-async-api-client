# ContentV2TagIdDelete400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**ResponseContentError5AdditionalErrors**](ResponseContentError5AdditionalErrors.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_tag_id_delete400_response import ContentV2TagIdDelete400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2TagIdDelete400Response from a JSON string
content_v2_tag_id_delete400_response_instance = ContentV2TagIdDelete400Response.from_json(json)
# print the JSON string representation of the object
print(ContentV2TagIdDelete400Response.to_json())

# convert the object into a dict
content_v2_tag_id_delete400_response_dict = content_v2_tag_id_delete400_response_instance.to_dict()
# create an instance of ContentV2TagIdDelete400Response from a dict
content_v2_tag_id_delete400_response_from_dict = ContentV2TagIdDelete400Response.from_dict(content_v2_tag_id_delete400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



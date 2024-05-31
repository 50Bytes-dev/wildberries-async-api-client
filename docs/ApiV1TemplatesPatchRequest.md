# ApiV1TemplatesPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Название шаблона (от 1 до 100 символов) | 
**template_id** | **int** | Идентификатор шаблона | 
**text** | **str** | Текст шаблона (от 2 до 1000 символов) | 

## Example

```python
from wildberries_async_api_client.models.api_v1_templates_patch_request import ApiV1TemplatesPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TemplatesPatchRequest from a JSON string
api_v1_templates_patch_request_instance = ApiV1TemplatesPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TemplatesPatchRequest.to_json())

# convert the object into a dict
api_v1_templates_patch_request_dict = api_v1_templates_patch_request_instance.to_dict()
# create an instance of ApiV1TemplatesPatchRequest from a dict
api_v1_templates_patch_request_from_dict = ApiV1TemplatesPatchRequest.from_dict(api_v1_templates_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1TemplatesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Название шаблона (от 1 до 100 символов) | 
**template_type** | **int** | Тип шаблона &lt;br&gt; &#x60;1&#x60; - шаблон для отзывов &lt;br&gt; &#x60;2&#x60; - шаблон для вопросов  | 
**text** | **str** | Текст шаблона (от 2 до 1000 символов) | 

## Example

```python
from wildberries_async_api_client.models.api_v1_templates_post_request import ApiV1TemplatesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TemplatesPostRequest from a JSON string
api_v1_templates_post_request_instance = ApiV1TemplatesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TemplatesPostRequest.to_json())

# convert the object into a dict
api_v1_templates_post_request_dict = api_v1_templates_post_request_instance.to_dict()
# create an instance of ApiV1TemplatesPostRequest from a dict
api_v1_templates_post_request_from_dict = ApiV1TemplatesPostRequest.from_dict(api_v1_templates_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1TemplatesDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **int** | Идентификатор шаблона (max. 1) | 

## Example

```python
from wildberries_async_api_client.models.api_v1_templates_delete_request import ApiV1TemplatesDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TemplatesDeleteRequest from a JSON string
api_v1_templates_delete_request_instance = ApiV1TemplatesDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1TemplatesDeleteRequest.to_json())

# convert the object into a dict
api_v1_templates_delete_request_dict = api_v1_templates_delete_request_instance.to_dict()
# create an instance of ApiV1TemplatesDeleteRequest from a dict
api_v1_templates_delete_request_from_dict = ApiV1TemplatesDeleteRequest.from_dict(api_v1_templates_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



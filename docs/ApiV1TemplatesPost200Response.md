# ApiV1TemplatesPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_templates_post200_response import ApiV1TemplatesPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1TemplatesPost200Response from a JSON string
api_v1_templates_post200_response_instance = ApiV1TemplatesPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1TemplatesPost200Response.to_json())

# convert the object into a dict
api_v1_templates_post200_response_dict = api_v1_templates_post200_response_instance.to_dict()
# create an instance of ApiV1TemplatesPost200Response from a dict
api_v1_templates_post200_response_from_dict = ApiV1TemplatesPost200Response.from_dict(api_v1_templates_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



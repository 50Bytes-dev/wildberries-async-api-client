# Response200DataTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор шаблона | [optional] 
**name** | **str** | Название шаблона | [optional] 
**text** | **str** | Текст шаблона | [optional] 

## Example

```python
from wildberries_async_api_client.models.response200_data_templates_inner import Response200DataTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of Response200DataTemplatesInner from a JSON string
response200_data_templates_inner_instance = Response200DataTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(Response200DataTemplatesInner.to_json())

# convert the object into a dict
response200_data_templates_inner_dict = response200_data_templates_inner_instance.to_dict()
# create an instance of Response200DataTemplatesInner from a dict
response200_data_templates_inner_from_dict = Response200DataTemplatesInner.from_dict(response200_data_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



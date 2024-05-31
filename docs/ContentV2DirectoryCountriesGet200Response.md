# ContentV2DirectoryCountriesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ContentV2DirectoryCountriesGet200ResponseDataInner]**](ContentV2DirectoryCountriesGet200ResponseDataInner.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **str** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_directory_countries_get200_response import ContentV2DirectoryCountriesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2DirectoryCountriesGet200Response from a JSON string
content_v2_directory_countries_get200_response_instance = ContentV2DirectoryCountriesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ContentV2DirectoryCountriesGet200Response.to_json())

# convert the object into a dict
content_v2_directory_countries_get200_response_dict = content_v2_directory_countries_get200_response_instance.to_dict()
# create an instance of ContentV2DirectoryCountriesGet200Response from a dict
content_v2_directory_countries_get200_response_from_dict = ContentV2DirectoryCountriesGet200Response.from_dict(content_v2_directory_countries_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



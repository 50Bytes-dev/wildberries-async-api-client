# ContentV2DirectoryTnvedGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tnved** | **str** | ТНВЭД-код | [optional] 
**is_kiz** | **bool** | - &#x60;true&#x60; - код маркировки требуется - &#x60;false&#x60; - код маркировки не требуется  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_directory_tnved_get200_response_data_inner import ContentV2DirectoryTnvedGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2DirectoryTnvedGet200ResponseDataInner from a JSON string
content_v2_directory_tnved_get200_response_data_inner_instance = ContentV2DirectoryTnvedGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2DirectoryTnvedGet200ResponseDataInner.to_json())

# convert the object into a dict
content_v2_directory_tnved_get200_response_data_inner_dict = content_v2_directory_tnved_get200_response_data_inner_instance.to_dict()
# create an instance of ContentV2DirectoryTnvedGet200ResponseDataInner from a dict
content_v2_directory_tnved_get200_response_data_inner_from_dict = ContentV2DirectoryTnvedGet200ResponseDataInner.from_dict(content_v2_directory_tnved_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



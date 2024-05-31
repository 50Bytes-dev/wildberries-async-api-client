# ContentV2TagIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Цвет тега | [optional] 
**name** | **str** | Имя тега | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_tag_id_patch_request import ContentV2TagIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2TagIdPatchRequest from a JSON string
content_v2_tag_id_patch_request_instance = ContentV2TagIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV2TagIdPatchRequest.to_json())

# convert the object into a dict
content_v2_tag_id_patch_request_dict = content_v2_tag_id_patch_request_instance.to_dict()
# create an instance of ContentV2TagIdPatchRequest from a dict
content_v2_tag_id_patch_request_from_dict = ContentV2TagIdPatchRequest.from_dict(content_v2_tag_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



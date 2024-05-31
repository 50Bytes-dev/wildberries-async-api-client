# ContentV2ObjectParentAllGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Название категории | [optional] 
**id** | **int** | Идентификатор родительской категории | [optional] 
**is_visible** | **bool** | Виден на сайте | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_object_parent_all_get200_response_data_inner import ContentV2ObjectParentAllGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2ObjectParentAllGet200ResponseDataInner from a JSON string
content_v2_object_parent_all_get200_response_data_inner_instance = ContentV2ObjectParentAllGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2ObjectParentAllGet200ResponseDataInner.to_json())

# convert the object into a dict
content_v2_object_parent_all_get200_response_data_inner_dict = content_v2_object_parent_all_get200_response_data_inner_instance.to_dict()
# create an instance of ContentV2ObjectParentAllGet200ResponseDataInner from a dict
content_v2_object_parent_all_get200_response_data_inner_from_dict = ContentV2ObjectParentAllGet200ResponseDataInner.from_dict(content_v2_object_parent_all_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



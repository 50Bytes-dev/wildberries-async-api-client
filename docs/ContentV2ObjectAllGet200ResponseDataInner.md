# ContentV2ObjectAllGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_id** | **int** | Идентификатор предмета | [optional] 
**parent_id** | **int** | Идентификатор родительской категории | [optional] 
**subject_name** | **str** | Название предмета | [optional] 
**parent_name** | **str** | Название родительской категории | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_object_all_get200_response_data_inner import ContentV2ObjectAllGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2ObjectAllGet200ResponseDataInner from a JSON string
content_v2_object_all_get200_response_data_inner_instance = ContentV2ObjectAllGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2ObjectAllGet200ResponseDataInner.to_json())

# convert the object into a dict
content_v2_object_all_get200_response_data_inner_dict = content_v2_object_all_get200_response_data_inner_instance.to_dict()
# create an instance of ContentV2ObjectAllGet200ResponseDataInner from a dict
content_v2_object_all_get200_response_data_inner_from_dict = ContentV2ObjectAllGet200ResponseDataInner.from_dict(content_v2_object_all_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



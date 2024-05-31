# ContentV3MediaSavePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | [optional] 
**data** | **List[str]** | Ссылки на изображения в том порядке, в котором они будут на карточке товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v3_media_save_post_request import ContentV3MediaSavePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV3MediaSavePostRequest from a JSON string
content_v3_media_save_post_request_instance = ContentV3MediaSavePostRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV3MediaSavePostRequest.to_json())

# convert the object into a dict
content_v3_media_save_post_request_dict = content_v3_media_save_post_request_instance.to_dict()
# create an instance of ContentV3MediaSavePostRequest from a dict
content_v3_media_save_post_request_from_dict = ContentV3MediaSavePostRequest.from_dict(content_v3_media_save_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



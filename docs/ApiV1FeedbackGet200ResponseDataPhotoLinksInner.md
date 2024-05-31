# ApiV1FeedbackGet200ResponseDataPhotoLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_size** | **str** | Адрес фотографии полного размера | [optional] 
**mini_size** | **str** | Адрес фотографии маленького размера | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedback_get200_response_data_photo_links_inner import ApiV1FeedbackGet200ResponseDataPhotoLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbackGet200ResponseDataPhotoLinksInner from a JSON string
api_v1_feedback_get200_response_data_photo_links_inner_instance = ApiV1FeedbackGet200ResponseDataPhotoLinksInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbackGet200ResponseDataPhotoLinksInner.to_json())

# convert the object into a dict
api_v1_feedback_get200_response_data_photo_links_inner_dict = api_v1_feedback_get200_response_data_photo_links_inner_instance.to_dict()
# create an instance of ApiV1FeedbackGet200ResponseDataPhotoLinksInner from a dict
api_v1_feedback_get200_response_data_photo_links_inner_from_dict = ApiV1FeedbackGet200ResponseDataPhotoLinksInner.from_dict(api_v1_feedback_get200_response_data_photo_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



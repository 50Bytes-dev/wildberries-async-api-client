# ApiV1FeedbackGet200ResponseDataVideo

Структура видео

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_image** | **str** | Ссылка на обложку видео | [optional] 
**link** | **str** | Ссылка на файл плейлиста видео (доступно по протоколу hls) | [optional] 
**duration_sec** | **int** | Общая продолжительность видео | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedback_get200_response_data_video import ApiV1FeedbackGet200ResponseDataVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbackGet200ResponseDataVideo from a JSON string
api_v1_feedback_get200_response_data_video_instance = ApiV1FeedbackGet200ResponseDataVideo.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbackGet200ResponseDataVideo.to_json())

# convert the object into a dict
api_v1_feedback_get200_response_data_video_dict = api_v1_feedback_get200_response_data_video_instance.to_dict()
# create an instance of ApiV1FeedbackGet200ResponseDataVideo from a dict
api_v1_feedback_get200_response_data_video_from_dict = ApiV1FeedbackGet200ResponseDataVideo.from_dict(api_v1_feedback_get200_response_data_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



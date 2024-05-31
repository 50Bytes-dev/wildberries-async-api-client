# ApiV1FeedbacksGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_unanswered** | **int** | Количество необработанных отзывов | [optional] 
**count_archive** | **int** | Количество обработанных отзывов | [optional] 
**feedbacks** | [**List[ResponseFeedbackInner]**](ResponseFeedbackInner.md) | Массив структур отзывов | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_get200_response_data import ApiV1FeedbacksGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksGet200ResponseData from a JSON string
api_v1_feedbacks_get200_response_data_instance = ApiV1FeedbacksGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksGet200ResponseData.to_json())

# convert the object into a dict
api_v1_feedbacks_get200_response_data_dict = api_v1_feedbacks_get200_response_data_instance.to_dict()
# create an instance of ApiV1FeedbacksGet200ResponseData from a dict
api_v1_feedbacks_get200_response_data_from_dict = ApiV1FeedbacksGet200ResponseData.from_dict(api_v1_feedbacks_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



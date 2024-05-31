# ApiV1FeedbacksOrderReturnPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feedback_id** | **str** | Идентификатор отзыва | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_order_return_post_request import ApiV1FeedbacksOrderReturnPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksOrderReturnPostRequest from a JSON string
api_v1_feedbacks_order_return_post_request_instance = ApiV1FeedbacksOrderReturnPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksOrderReturnPostRequest.to_json())

# convert the object into a dict
api_v1_feedbacks_order_return_post_request_dict = api_v1_feedbacks_order_return_post_request_instance.to_dict()
# create an instance of ApiV1FeedbacksOrderReturnPostRequest from a dict
api_v1_feedbacks_order_return_post_request_from_dict = ApiV1FeedbacksOrderReturnPostRequest.from_dict(api_v1_feedbacks_order_return_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



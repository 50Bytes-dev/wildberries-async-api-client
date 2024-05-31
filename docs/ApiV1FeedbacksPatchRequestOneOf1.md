# ApiV1FeedbacksPatchRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id отзыва | 
**text** | **str** | Текст ответа (max. 1000 символов) | 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_patch_request_one_of1 import ApiV1FeedbacksPatchRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksPatchRequestOneOf1 from a JSON string
api_v1_feedbacks_patch_request_one_of1_instance = ApiV1FeedbacksPatchRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksPatchRequestOneOf1.to_json())

# convert the object into a dict
api_v1_feedbacks_patch_request_one_of1_dict = api_v1_feedbacks_patch_request_one_of1_instance.to_dict()
# create an instance of ApiV1FeedbacksPatchRequestOneOf1 from a dict
api_v1_feedbacks_patch_request_one_of1_from_dict = ApiV1FeedbacksPatchRequestOneOf1.from_dict(api_v1_feedbacks_patch_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



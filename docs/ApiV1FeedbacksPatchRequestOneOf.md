# ApiV1FeedbacksPatchRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id отзыва | 
**was_viewed** | **bool** | Просмотрен (&#x60;true&#x60;) или не просмотрен (&#x60;false&#x60;) | 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_patch_request_one_of import ApiV1FeedbacksPatchRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksPatchRequestOneOf from a JSON string
api_v1_feedbacks_patch_request_one_of_instance = ApiV1FeedbacksPatchRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksPatchRequestOneOf.to_json())

# convert the object into a dict
api_v1_feedbacks_patch_request_one_of_dict = api_v1_feedbacks_patch_request_one_of_instance.to_dict()
# create an instance of ApiV1FeedbacksPatchRequestOneOf from a dict
api_v1_feedbacks_patch_request_one_of_from_dict = ApiV1FeedbacksPatchRequestOneOf.from_dict(api_v1_feedbacks_patch_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



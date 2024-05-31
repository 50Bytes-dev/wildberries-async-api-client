# ApiV1FeedbacksPatchRequestOneOf2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отзыва | 
**supplier_feedback_valuation** | **int** | Оценка отзыва. Можно получить методом &lt;b&gt;Получить список оценок&lt;/b&gt; | [optional] 
**supplier_product_valuation** | **int** | Оценка товара. Можно получить методом &lt;b&gt;Получить список оценок&lt;/b&gt; | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_patch_request_one_of2 import ApiV1FeedbacksPatchRequestOneOf2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksPatchRequestOneOf2 from a JSON string
api_v1_feedbacks_patch_request_one_of2_instance = ApiV1FeedbacksPatchRequestOneOf2.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksPatchRequestOneOf2.to_json())

# convert the object into a dict
api_v1_feedbacks_patch_request_one_of2_dict = api_v1_feedbacks_patch_request_one_of2_instance.to_dict()
# create an instance of ApiV1FeedbacksPatchRequestOneOf2 from a dict
api_v1_feedbacks_patch_request_one_of2_from_dict = ApiV1FeedbacksPatchRequestOneOf2.from_dict(api_v1_feedbacks_patch_request_one_of2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



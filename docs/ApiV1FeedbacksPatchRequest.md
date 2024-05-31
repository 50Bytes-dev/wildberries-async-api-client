# ApiV1FeedbacksPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отзыва | 
**was_viewed** | **bool** | Просмотрен (&#x60;true&#x60;) или не просмотрен (&#x60;false&#x60;) | 
**text** | **str** | Текст ответа (max. 1000 символов) | 
**supplier_feedback_valuation** | **int** | Оценка отзыва. Можно получить методом &lt;b&gt;Получить список оценок&lt;/b&gt; | [optional] 
**supplier_product_valuation** | **int** | Оценка товара. Можно получить методом &lt;b&gt;Получить список оценок&lt;/b&gt; | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_patch_request import ApiV1FeedbacksPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksPatchRequest from a JSON string
api_v1_feedbacks_patch_request_instance = ApiV1FeedbacksPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksPatchRequest.to_json())

# convert the object into a dict
api_v1_feedbacks_patch_request_dict = api_v1_feedbacks_patch_request_instance.to_dict()
# create an instance of ApiV1FeedbacksPatchRequest from a dict
api_v1_feedbacks_patch_request_from_dict = ApiV1FeedbacksPatchRequest.from_dict(api_v1_feedbacks_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



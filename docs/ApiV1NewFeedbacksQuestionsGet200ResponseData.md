# ApiV1NewFeedbacksQuestionsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_new_questions** | **bool** | Есть ли непросмотренные вопросы (&#x60;true&#x60; есть, &#x60;false&#x60; нет) | [optional] 
**has_new_feedbacks** | **bool** | Есть ли непросмотренные отзывы (&#x60;true&#x60; есть, &#x60;false&#x60; нет) | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_new_feedbacks_questions_get200_response_data import ApiV1NewFeedbacksQuestionsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1NewFeedbacksQuestionsGet200ResponseData from a JSON string
api_v1_new_feedbacks_questions_get200_response_data_instance = ApiV1NewFeedbacksQuestionsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1NewFeedbacksQuestionsGet200ResponseData.to_json())

# convert the object into a dict
api_v1_new_feedbacks_questions_get200_response_data_dict = api_v1_new_feedbacks_questions_get200_response_data_instance.to_dict()
# create an instance of ApiV1NewFeedbacksQuestionsGet200ResponseData from a dict
api_v1_new_feedbacks_questions_get200_response_data_from_dict = ApiV1NewFeedbacksQuestionsGet200ResponseData.from_dict(api_v1_new_feedbacks_questions_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



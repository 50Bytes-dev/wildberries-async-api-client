# ApiV1FeedbackGet200ResponseDataAnswer

Структура ответа

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Текст ответа | [optional] 
**state** | **str** | Статус:   - &#x60;none&#x60; - новый   - &#x60;wbRu&#x60;- отображается на сайте   - &#x60;reviewRequired&#x60; - ответ проходит проверку   - &#x60;rejected&#x60; - ответ отклонён  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedback_get200_response_data_answer import ApiV1FeedbackGet200ResponseDataAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbackGet200ResponseDataAnswer from a JSON string
api_v1_feedback_get200_response_data_answer_instance = ApiV1FeedbackGet200ResponseDataAnswer.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbackGet200ResponseDataAnswer.to_json())

# convert the object into a dict
api_v1_feedback_get200_response_data_answer_dict = api_v1_feedback_get200_response_data_answer_instance.to_dict()
# create an instance of ApiV1FeedbackGet200ResponseDataAnswer from a dict
api_v1_feedback_get200_response_data_answer_from_dict = ApiV1FeedbackGet200ResponseDataAnswer.from_dict(api_v1_feedback_get200_response_data_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ResponseFeedbackInnerAnswer

Структура ответа

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Текст ответа | [optional] 
**state** | **str** | Статус:   - &#x60;none&#x60; - новый   - &#x60;wbRu&#x60; - отображается на сайте   - &#x60;reviewRequired&#x60; - ответ проходит проверку   - &#x60;rejected&#x60; - ответ отклонён  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_feedback_inner_answer import ResponseFeedbackInnerAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseFeedbackInnerAnswer from a JSON string
response_feedback_inner_answer_instance = ResponseFeedbackInnerAnswer.from_json(json)
# print the JSON string representation of the object
print(ResponseFeedbackInnerAnswer.to_json())

# convert the object into a dict
response_feedback_inner_answer_dict = response_feedback_inner_answer_instance.to_dict()
# create an instance of ResponseFeedbackInnerAnswer from a dict
response_feedback_inner_answer_from_dict = ResponseFeedbackInnerAnswer.from_dict(response_feedback_inner_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer

Структура ответа

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Текст ответа | [optional] 
**editable** | **bool** | Можно ли отредактировать ответ (&#x60;false&#x60; - нельзя, &#x60;true&#x60; - можно) | [optional] 
**create_date** | **datetime** | Дата и время создания ответа | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_get200_response_data_questions_inner_answer import ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer from a JSON string
api_v1_questions_get200_response_data_questions_inner_answer_instance = ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer.to_json())

# convert the object into a dict
api_v1_questions_get200_response_data_questions_inner_answer_dict = api_v1_questions_get200_response_data_questions_inner_answer_instance.to_dict()
# create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer from a dict
api_v1_questions_get200_response_data_questions_inner_answer_from_dict = ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer.from_dict(api_v1_questions_get200_response_data_questions_inner_answer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



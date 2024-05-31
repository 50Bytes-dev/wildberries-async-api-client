# ApiV1QuestionsCountUnansweredGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_unanswered** | **int** | Количество неотвеченных вопросов | [optional] 
**count_unanswered_today** | **int** | Количество неотвеченных вопросов за сегодня | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_count_unanswered_get200_response_data import ApiV1QuestionsCountUnansweredGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsCountUnansweredGet200ResponseData from a JSON string
api_v1_questions_count_unanswered_get200_response_data_instance = ApiV1QuestionsCountUnansweredGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsCountUnansweredGet200ResponseData.to_json())

# convert the object into a dict
api_v1_questions_count_unanswered_get200_response_data_dict = api_v1_questions_count_unanswered_get200_response_data_instance.to_dict()
# create an instance of ApiV1QuestionsCountUnansweredGet200ResponseData from a dict
api_v1_questions_count_unanswered_get200_response_data_from_dict = ApiV1QuestionsCountUnansweredGet200ResponseData.from_dict(api_v1_questions_count_unanswered_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



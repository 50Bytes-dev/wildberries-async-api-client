# ApiV1QuestionsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_unanswered** | **int** | Количество необработанных вопросов | [optional] 
**count_archive** | **int** | Количество обработанных вопросов | [optional] 
**questions** | [**List[ApiV1QuestionsGet200ResponseDataQuestionsInner]**](ApiV1QuestionsGet200ResponseDataQuestionsInner.md) | Массив структур вопросов | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_get200_response_data import ApiV1QuestionsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsGet200ResponseData from a JSON string
api_v1_questions_get200_response_data_instance = ApiV1QuestionsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsGet200ResponseData.to_json())

# convert the object into a dict
api_v1_questions_get200_response_data_dict = api_v1_questions_get200_response_data_instance.to_dict()
# create an instance of ApiV1QuestionsGet200ResponseData from a dict
api_v1_questions_get200_response_data_from_dict = ApiV1QuestionsGet200ResponseData.from_dict(api_v1_questions_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



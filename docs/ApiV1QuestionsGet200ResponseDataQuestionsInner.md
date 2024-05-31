# ApiV1QuestionsGet200ResponseDataQuestionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id вопроса | [optional] 
**text** | **str** | Текст вопроса | [optional] 
**created_date** | **datetime** | Дата и время создания вопроса | [optional] 
**state** | **str** | Статус вопроса:   - &#x60;none&#x60; - вопрос отклонён продавцом (такой вопрос не отображается на портале покупателей)   - &#x60;wbRu&#x60; - ответ предоставлен, вопрос отображается на сайте покупателей   - &#x60;suppliersPortalSynch&#x60; - новый вопрос  | [optional] 
**answer** | [**ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer**](ApiV1QuestionsGet200ResponseDataQuestionsInnerAnswer.md) |  | [optional] 
**product_details** | [**ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails**](ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails.md) |  | [optional] 
**was_viewed** | **bool** | Просмотрен ли вопрос | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_get200_response_data_questions_inner import ApiV1QuestionsGet200ResponseDataQuestionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInner from a JSON string
api_v1_questions_get200_response_data_questions_inner_instance = ApiV1QuestionsGet200ResponseDataQuestionsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsGet200ResponseDataQuestionsInner.to_json())

# convert the object into a dict
api_v1_questions_get200_response_data_questions_inner_dict = api_v1_questions_get200_response_data_questions_inner_instance.to_dict()
# create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInner from a dict
api_v1_questions_get200_response_data_questions_inner_from_dict = ApiV1QuestionsGet200ResponseDataQuestionsInner.from_dict(api_v1_questions_get200_response_data_questions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



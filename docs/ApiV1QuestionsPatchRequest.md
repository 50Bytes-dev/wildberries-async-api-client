# ApiV1QuestionsPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id вопроса | 
**was_viewed** | **bool** | Просмотрен (&#x60;true&#x60;), не просмотрен (&#x60;false&#x60;) | 
**answer** | [**ApiV1QuestionsPatchRequestOneOf1Answer**](ApiV1QuestionsPatchRequestOneOf1Answer.md) |  | 
**state** | **str** | Статус вопроса:   - &#x60;none&#x60; - вопрос отклонён продавцом (такой вопрос не отображается на портале покупателей)   - &#x60;wbRu&#x60; - ответ предоставлен, вопрос отображается на сайте покупателей.  | 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_patch_request import ApiV1QuestionsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsPatchRequest from a JSON string
api_v1_questions_patch_request_instance = ApiV1QuestionsPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsPatchRequest.to_json())

# convert the object into a dict
api_v1_questions_patch_request_dict = api_v1_questions_patch_request_instance.to_dict()
# create an instance of ApiV1QuestionsPatchRequest from a dict
api_v1_questions_patch_request_from_dict = ApiV1QuestionsPatchRequest.from_dict(api_v1_questions_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



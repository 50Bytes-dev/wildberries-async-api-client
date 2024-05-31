# ApiV1QuestionsPatchRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id вопроса | 
**answer** | [**ApiV1QuestionsPatchRequestOneOf1Answer**](ApiV1QuestionsPatchRequestOneOf1Answer.md) |  | 
**state** | **str** | Статус вопроса:   - &#x60;none&#x60; - вопрос отклонён продавцом (такой вопрос не отображается на портале покупателей)   - &#x60;wbRu&#x60; - ответ предоставлен, вопрос отображается на сайте покупателей.  | 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_patch_request_one_of1 import ApiV1QuestionsPatchRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsPatchRequestOneOf1 from a JSON string
api_v1_questions_patch_request_one_of1_instance = ApiV1QuestionsPatchRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsPatchRequestOneOf1.to_json())

# convert the object into a dict
api_v1_questions_patch_request_one_of1_dict = api_v1_questions_patch_request_one_of1_instance.to_dict()
# create an instance of ApiV1QuestionsPatchRequestOneOf1 from a dict
api_v1_questions_patch_request_one_of1_from_dict = ApiV1QuestionsPatchRequestOneOf1.from_dict(api_v1_questions_patch_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



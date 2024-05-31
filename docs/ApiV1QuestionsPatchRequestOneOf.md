# ApiV1QuestionsPatchRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id вопроса | 
**was_viewed** | **bool** | Просмотрен (&#x60;true&#x60;), не просмотрен (&#x60;false&#x60;) | 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_patch_request_one_of import ApiV1QuestionsPatchRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsPatchRequestOneOf from a JSON string
api_v1_questions_patch_request_one_of_instance = ApiV1QuestionsPatchRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsPatchRequestOneOf.to_json())

# convert the object into a dict
api_v1_questions_patch_request_one_of_dict = api_v1_questions_patch_request_one_of_instance.to_dict()
# create an instance of ApiV1QuestionsPatchRequestOneOf from a dict
api_v1_questions_patch_request_one_of_from_dict = ApiV1QuestionsPatchRequestOneOf.from_dict(api_v1_questions_patch_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ResponsefeedbackErr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 
**request_id** | **str** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.responsefeedback_err import ResponsefeedbackErr

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsefeedbackErr from a JSON string
responsefeedback_err_instance = ResponsefeedbackErr.from_json(json)
# print the JSON string representation of the object
print(ResponsefeedbackErr.to_json())

# convert the object into a dict
responsefeedback_err_dict = responsefeedback_err_instance.to_dict()
# create an instance of ResponsefeedbackErr from a dict
responsefeedback_err_from_dict = ResponsefeedbackErr.from_dict(responsefeedback_err_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



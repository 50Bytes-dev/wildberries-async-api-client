# ResponseCardCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**ResponseCardCreateAdditionalErrors**](ResponseCardCreateAdditionalErrors.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_card_create import ResponseCardCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCardCreate from a JSON string
response_card_create_instance = ResponseCardCreate.from_json(json)
# print the JSON string representation of the object
print(ResponseCardCreate.to_json())

# convert the object into a dict
response_card_create_dict = response_card_create_instance.to_dict()
# create an instance of ResponseCardCreate from a dict
response_card_create_from_dict = ResponseCardCreate.from_dict(response_card_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Response429Daily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[object]** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response429_daily import Response429Daily

# TODO update the JSON string below
json = "{}"
# create an instance of Response429Daily from a JSON string
response429_daily_instance = Response429Daily.from_json(json)
# print the JSON string representation of the object
print(Response429Daily.to_json())

# convert the object into a dict
response429_daily_dict = response429_daily_instance.to_dict()
# create an instance of Response429Daily from a dict
response429_daily_from_dict = Response429Daily.from_dict(response429_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



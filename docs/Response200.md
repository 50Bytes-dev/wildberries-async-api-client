# Response200



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Response200Data**](Response200Data.md) |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **object** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response200 import Response200

# TODO update the JSON string below
json = "{}"
# create an instance of Response200 from a JSON string
response200_instance = Response200.from_json(json)
# print the JSON string representation of the object
print(Response200.to_json())

# convert the object into a dict
response200_dict = response200_instance.to_dict()
# create an instance of Response200 from a dict
response200_from_dict = Response200.from_dict(response200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



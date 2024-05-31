# Response429


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | [optional] 
**message** | **str** | Описание ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.response429 import Response429

# TODO update the JSON string below
json = "{}"
# create an instance of Response429 from a JSON string
response429_instance = Response429.from_json(json)
# print the JSON string representation of the object
print(Response429.to_json())

# convert the object into a dict
response429_dict = response429_instance.to_dict()
# create an instance of Response429 from a dict
response429_from_dict = Response429.from_dict(response429_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



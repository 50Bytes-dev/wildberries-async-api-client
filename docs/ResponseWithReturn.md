# ResponseWithReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Размер обновлённого бюджета | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_with_return import ResponseWithReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseWithReturn from a JSON string
response_with_return_instance = ResponseWithReturn.from_json(json)
# print the JSON string representation of the object
print(ResponseWithReturn.to_json())

# convert the object into a dict
response_with_return_dict = response_with_return_instance.to_dict()
# create an instance of ResponseWithReturn from a dict
response_with_return_from_dict = ResponseWithReturn.from_dict(response_with_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



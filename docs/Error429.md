# Error429


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.error429 import Error429

# TODO update the JSON string below
json = "{}"
# create an instance of Error429 from a JSON string
error429_instance = Error429.from_json(json)
# print the JSON string representation of the object
print(Error429.to_json())

# convert the object into a dict
error429_dict = error429_instance.to_dict()
# create an instance of Error429 from a dict
error429_from_dict = Error429.from_dict(error429_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



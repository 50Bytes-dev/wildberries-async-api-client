# Response200Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[Response200DataTemplatesInner]**](Response200DataTemplatesInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response200_data import Response200Data

# TODO update the JSON string below
json = "{}"
# create an instance of Response200Data from a JSON string
response200_data_instance = Response200Data.from_json(json)
# print the JSON string representation of the object
print(Response200Data.to_json())

# convert the object into a dict
response200_data_dict = response200_data_instance.to_dict()
# create an instance of Response200Data from a dict
response200_data_from_dict = Response200Data.from_dict(response200_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



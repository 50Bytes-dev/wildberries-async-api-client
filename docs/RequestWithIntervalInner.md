# RequestWithIntervalInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID кампании | [optional] 
**interval** | [**RequestWithIntervalInnerInterval**](RequestWithIntervalInnerInterval.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.request_with_interval_inner import RequestWithIntervalInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWithIntervalInner from a JSON string
request_with_interval_inner_instance = RequestWithIntervalInner.from_json(json)
# print the JSON string representation of the object
print(RequestWithIntervalInner.to_json())

# convert the object into a dict
request_with_interval_inner_dict = request_with_interval_inner_instance.to_dict()
# create an instance of RequestWithIntervalInner from a dict
request_with_interval_inner_from_dict = RequestWithIntervalInner.from_dict(request_with_interval_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RequestWithIntervalInnerInterval

Временной диапазон, за который необходимо выдать данные.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **date** | Начало запрашиваемого периода | [optional] 
**end** | **date** | Конец запрашиваемого периода | [optional] 

## Example

```python
from wildberries_async_api_client.models.request_with_interval_inner_interval import RequestWithIntervalInnerInterval

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWithIntervalInnerInterval from a JSON string
request_with_interval_inner_interval_instance = RequestWithIntervalInnerInterval.from_json(json)
# print the JSON string representation of the object
print(RequestWithIntervalInnerInterval.to_json())

# convert the object into a dict
request_with_interval_inner_interval_dict = request_with_interval_inner_interval_instance.to_dict()
# create an instance of RequestWithIntervalInnerInterval from a dict
request_with_interval_inner_interval_from_dict = RequestWithIntervalInnerInterval.from_dict(request_with_interval_inner_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



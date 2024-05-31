# ResponseErrorStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_error_statistics import ResponseErrorStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseErrorStatistics from a JSON string
response_error_statistics_instance = ResponseErrorStatistics.from_json(json)
# print the JSON string representation of the object
print(ResponseErrorStatistics.to_json())

# convert the object into a dict
response_error_statistics_dict = response_error_statistics_instance.to_dict()
# create an instance of ResponseErrorStatistics from a dict
response_error_statistics_from_dict = ResponseErrorStatistics.from_dict(response_error_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ExciseReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ModelsExciseReportResponse**](ModelsExciseReportResponse.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.excise_report_response import ExciseReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExciseReportResponse from a JSON string
excise_report_response_instance = ExciseReportResponse.from_json(json)
# print the JSON string representation of the object
print(ExciseReportResponse.to_json())

# convert the object into a dict
excise_report_response_dict = excise_report_response_instance.to_dict()
# create an instance of ExciseReportResponse from a dict
excise_report_response_from_dict = ExciseReportResponse.from_dict(excise_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



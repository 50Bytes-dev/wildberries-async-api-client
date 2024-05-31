# NmReportGetReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NmReportGetReportsResponseDataInner]**](NmReportGetReportsResponseDataInner.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Текст ошибки | [optional] 
**additional_errors** | [**List[NmReportGetReportsResponseAdditionalErrorsInner]**](NmReportGetReportsResponseAdditionalErrorsInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_get_reports_response import NmReportGetReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGetReportsResponse from a JSON string
nm_report_get_reports_response_instance = NmReportGetReportsResponse.from_json(json)
# print the JSON string representation of the object
print(NmReportGetReportsResponse.to_json())

# convert the object into a dict
nm_report_get_reports_response_dict = nm_report_get_reports_response_instance.to_dict()
# create an instance of NmReportGetReportsResponse from a dict
nm_report_get_reports_response_from_dict = NmReportGetReportsResponse.from_dict(nm_report_get_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



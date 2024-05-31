# NmReportRetryReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_id** | **str** | ID отчёта | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_retry_report_request import NmReportRetryReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportRetryReportRequest from a JSON string
nm_report_retry_report_request_instance = NmReportRetryReportRequest.from_json(json)
# print the JSON string representation of the object
print(NmReportRetryReportRequest.to_json())

# convert the object into a dict
nm_report_retry_report_request_dict = nm_report_retry_report_request_instance.to_dict()
# create an instance of NmReportRetryReportRequest from a dict
nm_report_retry_report_request_from_dict = NmReportRetryReportRequest.from_dict(nm_report_retry_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



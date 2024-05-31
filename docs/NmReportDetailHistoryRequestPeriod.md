# NmReportDetailHistoryRequestPeriod

Период

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **date** | Начало периода | [optional] 
**end** | **date** | Конец периода | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_history_request_period import NmReportDetailHistoryRequestPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailHistoryRequestPeriod from a JSON string
nm_report_detail_history_request_period_instance = NmReportDetailHistoryRequestPeriod.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailHistoryRequestPeriod.to_json())

# convert the object into a dict
nm_report_detail_history_request_period_dict = nm_report_detail_history_request_period_instance.to_dict()
# create an instance of NmReportDetailHistoryRequestPeriod from a dict
nm_report_detail_history_request_period_from_dict = NmReportDetailHistoryRequestPeriod.from_dict(nm_report_detail_history_request_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



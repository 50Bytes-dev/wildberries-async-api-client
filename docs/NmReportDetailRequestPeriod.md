# NmReportDetailRequestPeriod

Период

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** | Начало периода | [optional] 
**end** | **str** | Конец периода | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_request_period import NmReportDetailRequestPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailRequestPeriod from a JSON string
nm_report_detail_request_period_instance = NmReportDetailRequestPeriod.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailRequestPeriod.to_json())

# convert the object into a dict
nm_report_detail_request_period_dict = nm_report_detail_request_period_instance.to_dict()
# create an instance of NmReportDetailRequestPeriod from a dict
nm_report_detail_request_period_from_dict = NmReportDetailRequestPeriod.from_dict(nm_report_detail_request_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NmReportGroupedRequestPeriod

Период

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** | Начало периода | [optional] 
**end** | **str** | Конец периода | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_request_period import NmReportGroupedRequestPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedRequestPeriod from a JSON string
nm_report_grouped_request_period_instance = NmReportGroupedRequestPeriod.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedRequestPeriod.to_json())

# convert the object into a dict
nm_report_grouped_request_period_dict = nm_report_grouped_request_period_instance.to_dict()
# create an instance of NmReportGroupedRequestPeriod from a dict
nm_report_grouped_request_period_from_dict = NmReportGroupedRequestPeriod.from_dict(nm_report_grouped_request_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



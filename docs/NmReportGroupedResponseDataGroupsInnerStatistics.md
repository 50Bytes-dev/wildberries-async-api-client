# NmReportGroupedResponseDataGroupsInnerStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_period** | [**NmReportGroupedResponseDataGroupsInnerStatisticsSelectedPeriod**](NmReportGroupedResponseDataGroupsInnerStatisticsSelectedPeriod.md) |  | [optional] 
**previous_period** | [**NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod**](NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriod.md) |  | [optional] 
**period_comparison** | [**NmReportGroupedResponseDataGroupsInnerStatisticsPeriodComparison**](NmReportGroupedResponseDataGroupsInnerStatisticsPeriodComparison.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics import NmReportGroupedResponseDataGroupsInnerStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedResponseDataGroupsInnerStatistics from a JSON string
nm_report_grouped_response_data_groups_inner_statistics_instance = NmReportGroupedResponseDataGroupsInnerStatistics.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedResponseDataGroupsInnerStatistics.to_json())

# convert the object into a dict
nm_report_grouped_response_data_groups_inner_statistics_dict = nm_report_grouped_response_data_groups_inner_statistics_instance.to_dict()
# create an instance of NmReportGroupedResponseDataGroupsInnerStatistics from a dict
nm_report_grouped_response_data_groups_inner_statistics_from_dict = NmReportGroupedResponseDataGroupsInnerStatistics.from_dict(nm_report_grouped_response_data_groups_inner_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



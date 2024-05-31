# NmReportDetailResponseDataCardsInnerStatistics

Статистика

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_period** | [**NmReportDetailResponseDataCardsInnerStatisticsSelectedPeriod**](NmReportDetailResponseDataCardsInnerStatisticsSelectedPeriod.md) |  | [optional] 
**previous_period** | [**NmReportDetailResponseDataCardsInnerStatisticsPreviousPeriod**](NmReportDetailResponseDataCardsInnerStatisticsPreviousPeriod.md) |  | [optional] 
**period_comparison** | [**NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison**](NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_statistics import NmReportDetailResponseDataCardsInnerStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponseDataCardsInnerStatistics from a JSON string
nm_report_detail_response_data_cards_inner_statistics_instance = NmReportDetailResponseDataCardsInnerStatistics.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponseDataCardsInnerStatistics.to_json())

# convert the object into a dict
nm_report_detail_response_data_cards_inner_statistics_dict = nm_report_detail_response_data_cards_inner_statistics_instance.to_dict()
# create an instance of NmReportDetailResponseDataCardsInnerStatistics from a dict
nm_report_detail_response_data_cards_inner_statistics_from_dict = NmReportDetailResponseDataCardsInnerStatistics.from_dict(nm_report_detail_response_data_cards_inner_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



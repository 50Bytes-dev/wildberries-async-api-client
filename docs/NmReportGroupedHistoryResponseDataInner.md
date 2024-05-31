# NmReportGroupedHistoryResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**NmReportGroupedHistoryResponseDataInnerObject**](NmReportGroupedHistoryResponseDataInnerObject.md) |  | [optional] 
**brand_name** | **str** | Название бренда | [optional] 
**tag** | [**NmReportGroupedHistoryResponseDataInnerTag**](NmReportGroupedHistoryResponseDataInnerTag.md) |  | [optional] 
**history** | [**List[NmReportGroupedHistoryResponseDataInnerHistoryInner]**](NmReportGroupedHistoryResponseDataInnerHistoryInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner import NmReportGroupedHistoryResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedHistoryResponseDataInner from a JSON string
nm_report_grouped_history_response_data_inner_instance = NmReportGroupedHistoryResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedHistoryResponseDataInner.to_json())

# convert the object into a dict
nm_report_grouped_history_response_data_inner_dict = nm_report_grouped_history_response_data_inner_instance.to_dict()
# create an instance of NmReportGroupedHistoryResponseDataInner from a dict
nm_report_grouped_history_response_data_inner_from_dict = NmReportGroupedHistoryResponseDataInner.from_dict(nm_report_grouped_history_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



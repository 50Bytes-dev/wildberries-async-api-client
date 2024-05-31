# NmReportDetailHistoryResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**imt_name** | **str** | Наименование КТ | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**history** | [**List[NmReportDetailHistoryResponseDataInnerHistoryInner]**](NmReportDetailHistoryResponseDataInnerHistoryInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_history_response_data_inner import NmReportDetailHistoryResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailHistoryResponseDataInner from a JSON string
nm_report_detail_history_response_data_inner_instance = NmReportDetailHistoryResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailHistoryResponseDataInner.to_json())

# convert the object into a dict
nm_report_detail_history_response_data_inner_dict = nm_report_detail_history_response_data_inner_instance.to_dict()
# create an instance of NmReportDetailHistoryResponseDataInner from a dict
nm_report_detail_history_response_data_inner_from_dict = NmReportDetailHistoryResponseDataInner.from_dict(nm_report_detail_history_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



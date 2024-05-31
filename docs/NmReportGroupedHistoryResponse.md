# NmReportGroupedHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NmReportGroupedHistoryResponseDataInner]**](NmReportGroupedHistoryResponseDataInner.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_history_response import NmReportGroupedHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedHistoryResponse from a JSON string
nm_report_grouped_history_response_instance = NmReportGroupedHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedHistoryResponse.to_json())

# convert the object into a dict
nm_report_grouped_history_response_dict = nm_report_grouped_history_response_instance.to_dict()
# create an instance of NmReportGroupedHistoryResponse from a dict
nm_report_grouped_history_response_from_dict = NmReportGroupedHistoryResponse.from_dict(nm_report_grouped_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



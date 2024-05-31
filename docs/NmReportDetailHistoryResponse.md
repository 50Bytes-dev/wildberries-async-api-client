# NmReportDetailHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NmReportDetailHistoryResponseDataInner]**](NmReportDetailHistoryResponseDataInner.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_history_response import NmReportDetailHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailHistoryResponse from a JSON string
nm_report_detail_history_response_instance = NmReportDetailHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailHistoryResponse.to_json())

# convert the object into a dict
nm_report_detail_history_response_dict = nm_report_detail_history_response_instance.to_dict()
# create an instance of NmReportDetailHistoryResponse from a dict
nm_report_detail_history_response_from_dict = NmReportDetailHistoryResponse.from_dict(nm_report_detail_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



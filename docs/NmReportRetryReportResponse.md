# NmReportRetryReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Уведомление, что началась повторная генерация отчёта | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_retry_report_response import NmReportRetryReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportRetryReportResponse from a JSON string
nm_report_retry_report_response_instance = NmReportRetryReportResponse.from_json(json)
# print the JSON string representation of the object
print(NmReportRetryReportResponse.to_json())

# convert the object into a dict
nm_report_retry_report_response_dict = nm_report_retry_report_response_instance.to_dict()
# create an instance of NmReportRetryReportResponse from a dict
nm_report_retry_report_response_from_dict = NmReportRetryReportResponse.from_dict(nm_report_retry_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



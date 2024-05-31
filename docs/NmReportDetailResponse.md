# NmReportDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NmReportDetailResponseData**](NmReportDetailResponseData.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response import NmReportDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponse from a JSON string
nm_report_detail_response_instance = NmReportDetailResponse.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponse.to_json())

# convert the object into a dict
nm_report_detail_response_dict = nm_report_detail_response_instance.to_dict()
# create an instance of NmReportDetailResponse from a dict
nm_report_detail_response_from_dict = NmReportDetailResponse.from_dict(nm_report_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



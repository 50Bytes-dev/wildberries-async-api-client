# NmReportGroupedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**NmReportGroupedResponseData**](NmReportGroupedResponseData.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_response import NmReportGroupedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedResponse from a JSON string
nm_report_grouped_response_instance = NmReportGroupedResponse.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedResponse.to_json())

# convert the object into a dict
nm_report_grouped_response_dict = nm_report_grouped_response_instance.to_dict()
# create an instance of NmReportGroupedResponse from a dict
nm_report_grouped_response_from_dict = NmReportGroupedResponse.from_dict(nm_report_grouped_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



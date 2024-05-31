# ExciseReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **List[str]** | Код стран по стандарту ISO 3166-2. Чтобы получить данные по всем странам, оставьте параметр пустым  | [optional] 

## Example

```python
from wildberries_async_api_client.models.excise_report_request import ExciseReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExciseReportRequest from a JSON string
excise_report_request_instance = ExciseReportRequest.from_json(json)
# print the JSON string representation of the object
print(ExciseReportRequest.to_json())

# convert the object into a dict
excise_report_request_dict = excise_report_request_instance.to_dict()
# create an instance of ExciseReportRequest from a dict
excise_report_request_from_dict = ExciseReportRequest.from_dict(excise_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



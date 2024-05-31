# ApiV1AnalyticsAcceptanceReportGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**List[ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner]**](ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_analytics_acceptance_report_get200_response import ApiV1AnalyticsAcceptanceReportGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AnalyticsAcceptanceReportGet200Response from a JSON string
api_v1_analytics_acceptance_report_get200_response_instance = ApiV1AnalyticsAcceptanceReportGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1AnalyticsAcceptanceReportGet200Response.to_json())

# convert the object into a dict
api_v1_analytics_acceptance_report_get200_response_dict = api_v1_analytics_acceptance_report_get200_response_instance.to_dict()
# create an instance of ApiV1AnalyticsAcceptanceReportGet200Response from a dict
api_v1_analytics_acceptance_report_get200_response_from_dict = ApiV1AnalyticsAcceptanceReportGet200Response.from_dict(api_v1_analytics_acceptance_report_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



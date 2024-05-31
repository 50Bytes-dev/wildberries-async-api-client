# ApiV2NmReportDownloadsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отчёта в UUID-формате. Генерируется продавцом самостоятельно | 
**report_type** | **str** | Тип отчёта — &#x60;GROUPED_HISTORY_REPORT&#x60; | 
**user_report_name** | **str** | Название отчёта (если не указано, сформируется автоматически) | [optional] 
**params** | [**GroupedByObjectsBrandsAndTagsReqParams**](GroupedByObjectsBrandsAndTagsReqParams.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_nm_report_downloads_post_request import ApiV2NmReportDownloadsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2NmReportDownloadsPostRequest from a JSON string
api_v2_nm_report_downloads_post_request_instance = ApiV2NmReportDownloadsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV2NmReportDownloadsPostRequest.to_json())

# convert the object into a dict
api_v2_nm_report_downloads_post_request_dict = api_v2_nm_report_downloads_post_request_instance.to_dict()
# create an instance of ApiV2NmReportDownloadsPostRequest from a dict
api_v2_nm_report_downloads_post_request_from_dict = ApiV2NmReportDownloadsPostRequest.from_dict(api_v2_nm_report_downloads_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



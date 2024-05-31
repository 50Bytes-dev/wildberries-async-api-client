# ApiV2NmReportDownloadsFileDownloadIdGet429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | [optional] 
**message** | **str** | Описание ошибки | [optional] 
**data** | **List[object]** |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | [**List[ResponseErrorAdditionalErrorsInner]**](ResponseErrorAdditionalErrorsInner.md) | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_nm_report_downloads_file_download_id_get429_response import ApiV2NmReportDownloadsFileDownloadIdGet429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2NmReportDownloadsFileDownloadIdGet429Response from a JSON string
api_v2_nm_report_downloads_file_download_id_get429_response_instance = ApiV2NmReportDownloadsFileDownloadIdGet429Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2NmReportDownloadsFileDownloadIdGet429Response.to_json())

# convert the object into a dict
api_v2_nm_report_downloads_file_download_id_get429_response_dict = api_v2_nm_report_downloads_file_download_id_get429_response_instance.to_dict()
# create an instance of ApiV2NmReportDownloadsFileDownloadIdGet429Response from a dict
api_v2_nm_report_downloads_file_download_id_get429_response_from_dict = ApiV2NmReportDownloadsFileDownloadIdGet429Response.from_dict(api_v2_nm_report_downloads_file_download_id_get429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



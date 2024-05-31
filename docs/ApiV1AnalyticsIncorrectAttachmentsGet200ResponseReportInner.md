# ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Цена, ₽ | [optional] 
**var_date** | **str** | Дата | [optional] 
**lost_reason** | **str** | Причина удержания | [optional] 
**nm_id** | **int** | Артикул Wildberries | [optional] 
**photo_url** | **str** | Фото | [optional] 
**shk_id** | **int** | Штрихкод | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_analytics_incorrect_attachments_get200_response_report_inner import ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner from a JSON string
api_v1_analytics_incorrect_attachments_get200_response_report_inner_instance = ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner.to_json())

# convert the object into a dict
api_v1_analytics_incorrect_attachments_get200_response_report_inner_dict = api_v1_analytics_incorrect_attachments_get200_response_report_inner_instance.to_dict()
# create an instance of ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner from a dict
api_v1_analytics_incorrect_attachments_get200_response_report_inner_from_dict = ApiV1AnalyticsIncorrectAttachmentsGet200ResponseReportInner.from_dict(api_v1_analytics_incorrect_attachments_get200_response_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Количество товаров, шт. | [optional] 
**gi_create_date** | **date** | Дата создания поставки | [optional] 
**income_id** | **int** | Номер поставки | [optional] 
**nm_id** | **int** | Артикул Wildberries | [optional] 
**shkreate_date** | **date** | Дата приёмки | [optional] 
**subject_name** | **str** | Предмет (подкатегория) | [optional] 
**sum** | **int** | Суммарная стоимость приёмки, ₽ | [optional] 
**total** | **float** | Суммарная стоимость приёмки, ₽ с копейками | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_analytics_acceptance_report_get200_response_report_inner import ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner from a JSON string
api_v1_analytics_acceptance_report_get200_response_report_inner_instance = ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner.to_json())

# convert the object into a dict
api_v1_analytics_acceptance_report_get200_response_report_inner_dict = api_v1_analytics_acceptance_report_get200_response_report_inner_instance.to_dict()
# create an instance of ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner from a dict
api_v1_analytics_acceptance_report_get200_response_report_inner_from_dict = ApiV1AnalyticsAcceptanceReportGet200ResponseReportInner.from_dict(api_v1_analytics_acceptance_report_get200_response_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



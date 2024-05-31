# ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_height** | **float** | Фактическая высота, см | [optional] 
**actual_length** | **float** | Фактическая длина, см | [optional] 
**actual_volume** | **float** | Фактический объём, л | [optional] 
**actual_width** | **float** | Фактическая ширина, см | [optional] 
**var_date** | **str** | Дата измерения в формате RFC 3339. Для расчёта используются измерения за 30 дней, до начала отчётной недели | [optional] 
**dimension_difference** | **float** | Разница в габаритах, % | [optional] 
**height** | **float** | Высота из карточки, см | [optional] 
**length** | **float** | Длина из карточки, см | [optional] 
**log_warehouse_coef** | **float** | Коэффициент логистики и хранения для товара | [optional] 
**nm_id** | **int** | Артикул Wildberries | [optional] 
**photo_urls** | **str** | Фото измерений | [optional] 
**title** | **str** | Наименование товара | [optional] 
**volume** | **float** | Объём из карточки, л | [optional] 
**width** | **float** | Ширина из карточки, см | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_analytics_storage_coefficient_get200_response_report_inner import ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner from a JSON string
api_v1_analytics_storage_coefficient_get200_response_report_inner_instance = ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner.to_json())

# convert the object into a dict
api_v1_analytics_storage_coefficient_get200_response_report_inner_dict = api_v1_analytics_storage_coefficient_get200_response_report_inner_instance.to_dict()
# create an instance of ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner from a dict
api_v1_analytics_storage_coefficient_get200_response_report_inner_from_dict = ApiV1AnalyticsStorageCoefficientGet200ResponseReportInner.from_dict(api_v1_analytics_storage_coefficient_get200_response_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Сумма штрафа в копейках | [optional] 
**var_date** | **date** | Дата изменения характеристик товара на складе | [optional] 
**new_barcode** | **str** | Новый баркод в карточке товара | [optional] 
**new_color** | **str** | Новый цвет | [optional] 
**new_sa** | **str** | Новый артикул продавца | [optional] 
**new_shk_id** | **int** | Новый штрихкод товара в Wildberries | [optional] 
**new_size** | **str** | Новый размер | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**old_barcode** | **str** | Старый баркод из карточки товара | [optional] 
**old_color** | **str** | Старый цвет | [optional] 
**old_sa** | **str** | Старый артикул продавца | [optional] 
**old_shk_id** | **int** | Старый штрихкод товара в Wildberries | [optional] 
**old_size** | **str** | Старый размер | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_analytics_characteristics_change_get200_response_report_inner import ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner from a JSON string
api_v1_analytics_characteristics_change_get200_response_report_inner_instance = ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner.to_json())

# convert the object into a dict
api_v1_analytics_characteristics_change_get200_response_report_inner_dict = api_v1_analytics_characteristics_change_get200_response_report_inner_instance.to_dict()
# create an instance of ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner from a dict
api_v1_analytics_characteristics_change_get200_response_report_inner_from_dict = ApiV1AnalyticsCharacteristicsChangeGet200ResponseReportInner.from_dict(api_v1_analytics_characteristics_change_get200_response_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



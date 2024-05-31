# ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Сумма штрафа, руб | [optional] 
**var_date** | **datetime** | Дата | [optional] 
**income_id** | **int** | Номер поставки | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**photo_urls** | **List[str]** | URL фото товара | [optional] 
**shk_id** | **int** | Штрихкод товара в Wildberries | [optional] 
**sku** | **str** | Баркод из карточки товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_analytics_goods_labeling_get200_response_report_inner import ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner from a JSON string
api_v1_analytics_goods_labeling_get200_response_report_inner_instance = ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner.to_json())

# convert the object into a dict
api_v1_analytics_goods_labeling_get200_response_report_inner_dict = api_v1_analytics_goods_labeling_get200_response_report_inner_instance.to_dict()
# create an instance of ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner from a dict
api_v1_analytics_goods_labeling_get200_response_report_inner_from_dict = ApiV1AnalyticsGoodsLabelingGet200ResponseReportInner.from_dict(api_v1_analytics_goods_labeling_get200_response_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



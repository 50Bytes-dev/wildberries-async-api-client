# NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions

Конверсии

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_cart_percent** | **float** | Конверсия в корзину, % (Какой процент посетителей, открывших карточку товара, добавили товар в корзину) | [optional] 
**cart_to_order_percent** | **float** | Конверсия в заказ, % (Какой процент посетителей, добавивших товар в корзину, сделали заказ) | [optional] 
**buyouts_percent** | **float** | Процент выкупа, % (Какой процент посетителей, заказавших товар, его выкупили. Без учёта товаров, которые еще доставляются покупателю.) | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions import NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions from a JSON string
nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions_instance = NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions.to_json())

# convert the object into a dict
nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions_dict = nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions_instance.to_dict()
# create an instance of NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions from a dict
nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions_from_dict = NmReportGroupedResponseDataGroupsInnerStatisticsPreviousPeriodConversions.from_dict(nm_report_grouped_response_data_groups_inner_statistics_previous_period_conversions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



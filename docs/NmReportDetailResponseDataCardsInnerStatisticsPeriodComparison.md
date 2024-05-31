# NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison

Сравнение двух периодов, в процентах

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_card_dynamics** | **int** | Динамика переходов в карточку товара | [optional] 
**add_to_cart_dynamics** | **int** | Динамика добавлений в корзину | [optional] 
**orders_count_dynamics** | **int** | Динамика количества заказов | [optional] 
**orders_sum_rub_dynamics** | **int** | Динамика суммы заказов, рублей | [optional] 
**buyouts_count_dynamics** | **int** | Динамика выкупов, штук | [optional] 
**buyouts_sum_rub_dynamics** | **int** | Динамика суммы выкупов, рублей | [optional] 
**cancel_count_dynamics** | **int** | Динамика отмен товаров, штук | [optional] 
**cancel_sum_rub_dynamics** | **int** | Динамика сумм отмен товаров, рублей | [optional] 
**avg_orders_count_per_day_dynamics** | **int** | Динамика среднего количества заказов в день | [optional] 
**avg_price_rub_dynamics** | **int** | Динамика средней цены на товары. Учитываются скидки для акций и WB скидка. | [optional] 
**conversions** | [**NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions**](NmReportDetailResponseDataCardsInnerStatisticsPeriodComparisonConversions.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_statistics_period_comparison import NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison from a JSON string
nm_report_detail_response_data_cards_inner_statistics_period_comparison_instance = NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison.to_json())

# convert the object into a dict
nm_report_detail_response_data_cards_inner_statistics_period_comparison_dict = nm_report_detail_response_data_cards_inner_statistics_period_comparison_instance.to_dict()
# create an instance of NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison from a dict
nm_report_detail_response_data_cards_inner_statistics_period_comparison_from_dict = NmReportDetailResponseDataCardsInnerStatisticsPeriodComparison.from_dict(nm_report_detail_response_data_cards_inner_statistics_period_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



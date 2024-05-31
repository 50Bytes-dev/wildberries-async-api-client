# NmReportGroupedHistoryResponseDataInnerHistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt** | **date** |  | [optional] 
**open_card_count** | **int** | Количество переходов в карточку товара | [optional] 
**add_to_cart_count** | **int** | Положили в корзину, штук | [optional] 
**orders_count** | **int** | Заказали товаров, шт | [optional] 
**orders_sum_rub** | **int** | Заказали на сумму, руб. | [optional] 
**buyouts_count** | **int** | Выкупили товаров, шт. | [optional] 
**buyouts_sum_rub** | **int** | Выкупили на сумму, руб. | [optional] 
**buyout_percent** | **int** | Процент выкупа, % (Какой процент посетителей, заказавших товар, его выкупили. Без учёта товаров, которые еще доставляются покупателю.) | [optional] 
**add_to_cart_conversion** | **int** | Конверсия в корзину, % (Какой процент посетителей, открывших карточку товара, добавили товар в корзину) | [optional] 
**cart_to_order_conversion** | **int** | Конверсия в заказ, % (Какой процент посетителей, добавивших товар в корзину, сделали заказ) | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_history_response_data_inner_history_inner import NmReportGroupedHistoryResponseDataInnerHistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedHistoryResponseDataInnerHistoryInner from a JSON string
nm_report_grouped_history_response_data_inner_history_inner_instance = NmReportGroupedHistoryResponseDataInnerHistoryInner.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedHistoryResponseDataInnerHistoryInner.to_json())

# convert the object into a dict
nm_report_grouped_history_response_data_inner_history_inner_dict = nm_report_grouped_history_response_data_inner_history_inner_instance.to_dict()
# create an instance of NmReportGroupedHistoryResponseDataInnerHistoryInner from a dict
nm_report_grouped_history_response_data_inner_history_inner_from_dict = NmReportGroupedHistoryResponseDataInnerHistoryInner.from_dict(nm_report_grouped_history_response_data_inner_history_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



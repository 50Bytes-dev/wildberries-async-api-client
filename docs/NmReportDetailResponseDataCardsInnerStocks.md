# NmReportDetailResponseDataCardsInnerStocks

Остатки

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stocks_mp** | **int** | Остатки МП, шт. (Общее количество остатков на складе продавца) | [optional] 
**stocks_wb** | **int** | Остатки на складах Wildberries (Общее количество остатков на складах Wildberries) | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_stocks import NmReportDetailResponseDataCardsInnerStocks

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponseDataCardsInnerStocks from a JSON string
nm_report_detail_response_data_cards_inner_stocks_instance = NmReportDetailResponseDataCardsInnerStocks.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponseDataCardsInnerStocks.to_json())

# convert the object into a dict
nm_report_detail_response_data_cards_inner_stocks_dict = nm_report_detail_response_data_cards_inner_stocks_instance.to_dict()
# create an instance of NmReportDetailResponseDataCardsInnerStocks from a dict
nm_report_detail_response_data_cards_inner_stocks_from_dict = NmReportDetailResponseDataCardsInnerStocks.from_dict(nm_report_detail_response_data_cards_inner_stocks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



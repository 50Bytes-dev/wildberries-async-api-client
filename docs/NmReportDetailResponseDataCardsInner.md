# NmReportDetailResponseDataCardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**brand_name** | **str** | Название бренд | [optional] 
**tags** | [**List[NmReportDetailResponseDataCardsInnerTagsInner]**](NmReportDetailResponseDataCardsInnerTagsInner.md) | Теги | [optional] 
**object** | [**NmReportDetailResponseDataCardsInnerObject**](NmReportDetailResponseDataCardsInnerObject.md) |  | [optional] 
**statistics** | [**NmReportDetailResponseDataCardsInnerStatistics**](NmReportDetailResponseDataCardsInnerStatistics.md) |  | [optional] 
**stocks** | [**NmReportDetailResponseDataCardsInnerStocks**](NmReportDetailResponseDataCardsInnerStocks.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner import NmReportDetailResponseDataCardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponseDataCardsInner from a JSON string
nm_report_detail_response_data_cards_inner_instance = NmReportDetailResponseDataCardsInner.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponseDataCardsInner.to_json())

# convert the object into a dict
nm_report_detail_response_data_cards_inner_dict = nm_report_detail_response_data_cards_inner_instance.to_dict()
# create an instance of NmReportDetailResponseDataCardsInner from a dict
nm_report_detail_response_data_cards_inner_from_dict = NmReportDetailResponseDataCardsInner.from_dict(nm_report_detail_response_data_cards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



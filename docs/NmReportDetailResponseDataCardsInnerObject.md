# NmReportDetailResponseDataCardsInnerObject

Предмет

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор предмета | [optional] 
**name** | **str** | Название предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_response_data_cards_inner_object import NmReportDetailResponseDataCardsInnerObject

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailResponseDataCardsInnerObject from a JSON string
nm_report_detail_response_data_cards_inner_object_instance = NmReportDetailResponseDataCardsInnerObject.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailResponseDataCardsInnerObject.to_json())

# convert the object into a dict
nm_report_detail_response_data_cards_inner_object_dict = nm_report_detail_response_data_cards_inner_object_instance.to_dict()
# create an instance of NmReportDetailResponseDataCardsInnerObject from a dict
nm_report_detail_response_data_cards_inner_object_from_dict = NmReportDetailResponseDataCardsInnerObject.from_dict(nm_report_detail_response_data_cards_inner_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



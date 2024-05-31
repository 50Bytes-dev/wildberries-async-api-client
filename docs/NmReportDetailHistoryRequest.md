# NmReportDetailHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_ids** | **List[int]** | Артикул Wildberries (максимум 20) | 
**period** | [**NmReportDetailHistoryRequestPeriod**](NmReportDetailHistoryRequestPeriod.md) |  | 
**timezone** | **str** | Временная зона.&lt;br&gt; Если не указано, то по умолчанию используется Europe/Moscow.  | [optional] 
**aggregation_level** | **str** | Тип агрегации. Если не указано, то по умолчанию используется агрегация по дням. &lt;br&gt; Доступные уровни агрегации &#x60;day&#x60;, &#x60;week&#x60;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_history_request import NmReportDetailHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailHistoryRequest from a JSON string
nm_report_detail_history_request_instance = NmReportDetailHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailHistoryRequest.to_json())

# convert the object into a dict
nm_report_detail_history_request_dict = nm_report_detail_history_request_instance.to_dict()
# create an instance of NmReportDetailHistoryRequest from a dict
nm_report_detail_history_request_from_dict = NmReportDetailHistoryRequest.from_dict(nm_report_detail_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



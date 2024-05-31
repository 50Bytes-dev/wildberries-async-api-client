# NmReportDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_names** | **List[str]** | Название бренда | [optional] 
**object_ids** | **List[int]** | Идентификатор предмета | [optional] 
**tag_ids** | **List[int]** | Идентификатор тега | [optional] 
**nm_ids** | **List[int]** | Артикул WB | [optional] 
**timezone** | **str** | Временная зона.&lt;br&gt; Если не указано, то по умолчанию используется Europe/Moscow.  | [optional] 
**period** | [**NmReportDetailRequestPeriod**](NmReportDetailRequestPeriod.md) |  | 
**order_by** | [**NmReportDetailRequestOrderBy**](NmReportDetailRequestOrderBy.md) |  | [optional] 
**page** | **int** | Страница | 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_request import NmReportDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailRequest from a JSON string
nm_report_detail_request_instance = NmReportDetailRequest.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailRequest.to_json())

# convert the object into a dict
nm_report_detail_request_dict = nm_report_detail_request_instance.to_dict()
# create an instance of NmReportDetailRequest from a dict
nm_report_detail_request_from_dict = NmReportDetailRequest.from_dict(nm_report_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



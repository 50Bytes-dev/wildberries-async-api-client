# NmReportGroupedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_ids** | **List[int]** | Идентификатор предмета | [optional] 
**brand_names** | **List[str]** | Название бренда | [optional] 
**tag_ids** | **List[int]** | Идентификатор тега | [optional] 
**timezone** | **str** | Временная зона.&lt;br&gt; Если не указано, то по умолчанию используется Europe/Moscow.              | [optional] 
**period** | [**NmReportGroupedRequestPeriod**](NmReportGroupedRequestPeriod.md) |  | 
**order_by** | [**NmReportGroupedRequestOrderBy**](NmReportGroupedRequestOrderBy.md) |  | [optional] 
**page** | **int** | Страница | 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_request import NmReportGroupedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedRequest from a JSON string
nm_report_grouped_request_instance = NmReportGroupedRequest.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedRequest.to_json())

# convert the object into a dict
nm_report_grouped_request_dict = nm_report_grouped_request_instance.to_dict()
# create an instance of NmReportGroupedRequest from a dict
nm_report_grouped_request_from_dict = NmReportGroupedRequest.from_dict(nm_report_grouped_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



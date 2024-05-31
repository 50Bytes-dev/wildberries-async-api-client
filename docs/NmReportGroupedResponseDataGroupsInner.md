# NmReportGroupedResponseDataGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** | Название бренда | [optional] 
**tags** | [**List[NmReportDetailResponseDataCardsInnerTagsInner]**](NmReportDetailResponseDataCardsInnerTagsInner.md) |  | [optional] 
**object** | [**NmReportGroupedResponseDataGroupsInnerObject**](NmReportGroupedResponseDataGroupsInnerObject.md) |  | [optional] 
**statistics** | [**NmReportGroupedResponseDataGroupsInnerStatistics**](NmReportGroupedResponseDataGroupsInnerStatistics.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_response_data_groups_inner import NmReportGroupedResponseDataGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedResponseDataGroupsInner from a JSON string
nm_report_grouped_response_data_groups_inner_instance = NmReportGroupedResponseDataGroupsInner.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedResponseDataGroupsInner.to_json())

# convert the object into a dict
nm_report_grouped_response_data_groups_inner_dict = nm_report_grouped_response_data_groups_inner_instance.to_dict()
# create an instance of NmReportGroupedResponseDataGroupsInner from a dict
nm_report_grouped_response_data_groups_inner_from_dict = NmReportGroupedResponseDataGroupsInner.from_dict(nm_report_grouped_response_data_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



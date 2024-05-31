# NmReportGroupedResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Страница | [optional] 
**is_next_page** | **bool** | Есть ли следующая страница (false - нет, true - есть) | [optional] 
**groups** | [**List[NmReportGroupedResponseDataGroupsInner]**](NmReportGroupedResponseDataGroupsInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_grouped_response_data import NmReportGroupedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGroupedResponseData from a JSON string
nm_report_grouped_response_data_instance = NmReportGroupedResponseData.from_json(json)
# print the JSON string representation of the object
print(NmReportGroupedResponseData.to_json())

# convert the object into a dict
nm_report_grouped_response_data_dict = nm_report_grouped_response_data_instance.to_dict()
# create an instance of NmReportGroupedResponseData from a dict
nm_report_grouped_response_data_from_dict = NmReportGroupedResponseData.from_dict(nm_report_grouped_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



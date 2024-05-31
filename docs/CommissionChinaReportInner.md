# CommissionChinaReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kgvp_china** | **float** | Комиссия для продавцов из Китая, % | [optional] 
**parent_id** | **int** | ID родительской категории | [optional] 
**parent_name** | **str** | Название родительской категории | [optional] 
**subject_id** | **int** | ID предмета | [optional] 
**subject_name** | **str** | Название предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_china_report_inner import CommissionChinaReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionChinaReportInner from a JSON string
commission_china_report_inner_instance = CommissionChinaReportInner.from_json(json)
# print the JSON string representation of the object
print(CommissionChinaReportInner.to_json())

# convert the object into a dict
commission_china_report_inner_dict = commission_china_report_inner_instance.to_dict()
# create an instance of CommissionChinaReportInner from a dict
commission_china_report_inner_from_dict = CommissionChinaReportInner.from_dict(commission_china_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



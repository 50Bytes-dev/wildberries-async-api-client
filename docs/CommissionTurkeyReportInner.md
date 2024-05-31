# CommissionTurkeyReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kgvp_turkey** | **float** | Комиссия для продавцов из Турции, % | [optional] 
**parent_id** | **int** | ID родительской категории | [optional] 
**parent_name** | **str** | Название родительской категории | [optional] 
**subject_id** | **int** | ID предмета | [optional] 
**subject_name** | **str** | Название предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_turkey_report_inner import CommissionTurkeyReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionTurkeyReportInner from a JSON string
commission_turkey_report_inner_instance = CommissionTurkeyReportInner.from_json(json)
# print the JSON string representation of the object
print(CommissionTurkeyReportInner.to_json())

# convert the object into a dict
commission_turkey_report_inner_dict = commission_turkey_report_inner_instance.to_dict()
# create an instance of CommissionTurkeyReportInner from a dict
commission_turkey_report_inner_from_dict = CommissionTurkeyReportInner.from_dict(commission_turkey_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



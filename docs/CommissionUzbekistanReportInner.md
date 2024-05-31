# CommissionUzbekistanReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kgvp_uzbekistan** | **float** | Комиссия для продавцов из Узбекистана, % | [optional] 
**parent_id** | **int** | ID родительской категории | [optional] 
**parent_name** | **str** | Название родительской категории | [optional] 
**subject_id** | **int** | ID предмета | [optional] 
**subject_name** | **str** | Название предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_uzbekistan_report_inner import CommissionUzbekistanReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionUzbekistanReportInner from a JSON string
commission_uzbekistan_report_inner_instance = CommissionUzbekistanReportInner.from_json(json)
# print the JSON string representation of the object
print(CommissionUzbekistanReportInner.to_json())

# convert the object into a dict
commission_uzbekistan_report_inner_dict = commission_uzbekistan_report_inner_instance.to_dict()
# create an instance of CommissionUzbekistanReportInner from a dict
commission_uzbekistan_report_inner_from_dict = CommissionUzbekistanReportInner.from_dict(commission_uzbekistan_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



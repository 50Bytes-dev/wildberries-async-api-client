# CommissionReportInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kgvp_marketplace** | **float** | Комиссия по модели &#x60;Склад продавца — везу на склад WB&#x60;, % | [optional] 
**kgvp_supplier** | **float** | Комиссия по моделям &#x60;Склад продавца — везу самостоятельно до клиента&#x60; и &#x60;Склад продавца — Курьером WB&#x60;, % | [optional] 
**kgvp_supplier_express** | **float** | Комиссия по модели &#x60;Склад продавца — везу самостоятельно до клиента экспресс&#x60;, % | [optional] 
**paid_storage_kgvp** | **float** | Комиссия по модели &#x60;Склад WB&#x60;, % | [optional] 
**parent_id** | **int** | ID родительской категории | [optional] 
**parent_name** | **str** | Название родительской категории | [optional] 
**subject_id** | **int** | ID предмета | [optional] 
**subject_name** | **str** | Название предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_report_inner import CommissionReportInner

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionReportInner from a JSON string
commission_report_inner_instance = CommissionReportInner.from_json(json)
# print the JSON string representation of the object
print(CommissionReportInner.to_json())

# convert the object into a dict
commission_report_inner_dict = commission_report_inner_instance.to_dict()
# create an instance of CommissionReportInner from a dict
commission_report_inner_from_dict = CommissionReportInner.from_dict(commission_report_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV1SearchSupplierSubjectsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор предмета | [optional] 
**name** | **str** | Название предмета | [optional] 
**nms_count** | **int** | Количество артикулов WB с этим предметом | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_search_supplier_subjects_get200_response_inner import AdvV1SearchSupplierSubjectsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1SearchSupplierSubjectsGet200ResponseInner from a JSON string
adv_v1_search_supplier_subjects_get200_response_inner_instance = AdvV1SearchSupplierSubjectsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1SearchSupplierSubjectsGet200ResponseInner.to_json())

# convert the object into a dict
adv_v1_search_supplier_subjects_get200_response_inner_dict = adv_v1_search_supplier_subjects_get200_response_inner_instance.to_dict()
# create an instance of AdvV1SearchSupplierSubjectsGet200ResponseInner from a dict
adv_v1_search_supplier_subjects_get200_response_inner_from_dict = AdvV1SearchSupplierSubjectsGet200ResponseInner.from_dict(adv_v1_search_supplier_subjects_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



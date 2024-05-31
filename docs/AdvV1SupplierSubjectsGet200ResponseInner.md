# AdvV1SupplierSubjectsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID предмета | [optional] 
**name** | **str** | Предмет | [optional] 
**count** | **int** | Количество Артикулов Wildberries (&#x60;nmId&#x60;) с таким предметом. | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_supplier_subjects_get200_response_inner import AdvV1SupplierSubjectsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1SupplierSubjectsGet200ResponseInner from a JSON string
adv_v1_supplier_subjects_get200_response_inner_instance = AdvV1SupplierSubjectsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1SupplierSubjectsGet200ResponseInner.to_json())

# convert the object into a dict
adv_v1_supplier_subjects_get200_response_inner_dict = adv_v1_supplier_subjects_get200_response_inner_instance.to_dict()
# create an instance of AdvV1SupplierSubjectsGet200ResponseInner from a dict
adv_v1_supplier_subjects_get200_response_inner_from_dict = AdvV1SupplierSubjectsGet200ResponseInner.from_dict(adv_v1_supplier_subjects_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



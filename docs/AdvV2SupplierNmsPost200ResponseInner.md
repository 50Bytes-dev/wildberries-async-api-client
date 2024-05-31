# AdvV2SupplierNmsPost200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Название товара | [optional] 
**nm** | **int** | Артикул Wildberries (&#x60;nmId&#x60;) | [optional] 
**subject_id** | **int** | ID предмета | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v2_supplier_nms_post200_response_inner import AdvV2SupplierNmsPost200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV2SupplierNmsPost200ResponseInner from a JSON string
adv_v2_supplier_nms_post200_response_inner_instance = AdvV2SupplierNmsPost200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV2SupplierNmsPost200ResponseInner.to_json())

# convert the object into a dict
adv_v2_supplier_nms_post200_response_inner_dict = adv_v2_supplier_nms_post200_response_inner_instance.to_dict()
# create an instance of AdvV2SupplierNmsPost200ResponseInner from a dict
adv_v2_supplier_nms_post200_response_inner_from_dict = AdvV2SupplierNmsPost200ResponseInner.from_dict(adv_v2_supplier_nms_post200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



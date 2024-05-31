# AdvV1SearchSupplierProductsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm** | **int** | Артикул WB. | [optional] 
**name** | **object** | Наименование товара. | [optional] 
**subject** | [**AdvV1SearchSupplierProductsGet200ResponseInnerSubject**](AdvV1SearchSupplierProductsGet200ResponseInnerSubject.md) |  | [optional] 
**brand** | **str** | Бренд. | [optional] 
**kind** | [**AdvV1SearchSupplierProductsGet200ResponseInnerKind**](AdvV1SearchSupplierProductsGet200ResponseInnerKind.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_search_supplier_products_get200_response_inner import AdvV1SearchSupplierProductsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1SearchSupplierProductsGet200ResponseInner from a JSON string
adv_v1_search_supplier_products_get200_response_inner_instance = AdvV1SearchSupplierProductsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1SearchSupplierProductsGet200ResponseInner.to_json())

# convert the object into a dict
adv_v1_search_supplier_products_get200_response_inner_dict = adv_v1_search_supplier_products_get200_response_inner_instance.to_dict()
# create an instance of AdvV1SearchSupplierProductsGet200ResponseInner from a dict
adv_v1_search_supplier_products_get200_response_inner_from_dict = AdvV1SearchSupplierProductsGet200ResponseInner.from_dict(adv_v1_search_supplier_products_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



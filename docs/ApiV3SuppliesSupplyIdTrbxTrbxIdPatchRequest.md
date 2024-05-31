# ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[int]** | Список заказов, которые необходимо добавить в короб. | 

## Example

```python
from wb_client.models.api_v3_supplies_supply_id_trbx_trbx_id_patch_request import ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest from a JSON string
api_v3_supplies_supply_id_trbx_trbx_id_patch_request_instance = ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest.to_json())

# convert the object into a dict
api_v3_supplies_supply_id_trbx_trbx_id_patch_request_dict = api_v3_supplies_supply_id_trbx_trbx_id_patch_request_instance.to_dict()
# create an instance of ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest from a dict
api_v3_supplies_supply_id_trbx_trbx_id_patch_request_from_dict = ApiV3SuppliesSupplyIdTrbxTrbxIdPatchRequest.from_dict(api_v3_supplies_supply_id_trbx_trbx_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



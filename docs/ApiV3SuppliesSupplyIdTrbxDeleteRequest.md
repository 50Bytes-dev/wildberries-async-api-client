# ApiV3SuppliesSupplyIdTrbxDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trbx_ids** | **List[str]** | Список ID коробов, которые необходимо удалить. | 

## Example

```python
from wb_client.models.api_v3_supplies_supply_id_trbx_delete_request import ApiV3SuppliesSupplyIdTrbxDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SuppliesSupplyIdTrbxDeleteRequest from a JSON string
api_v3_supplies_supply_id_trbx_delete_request_instance = ApiV3SuppliesSupplyIdTrbxDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3SuppliesSupplyIdTrbxDeleteRequest.to_json())

# convert the object into a dict
api_v3_supplies_supply_id_trbx_delete_request_dict = api_v3_supplies_supply_id_trbx_delete_request_instance.to_dict()
# create an instance of ApiV3SuppliesSupplyIdTrbxDeleteRequest from a dict
api_v3_supplies_supply_id_trbx_delete_request_from_dict = ApiV3SuppliesSupplyIdTrbxDeleteRequest.from_dict(api_v3_supplies_supply_id_trbx_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



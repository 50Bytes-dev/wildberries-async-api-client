# SupplyTrbx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID короба. | [optional] 
**orders** | **List[int]** | Массив идентификаторов заказа. | [optional] 

## Example

```python
from wb_client.models.supply_trbx import SupplyTrbx

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyTrbx from a JSON string
supply_trbx_instance = SupplyTrbx.from_json(json)
# print the JSON string representation of the object
print(SupplyTrbx.to_json())

# convert the object into a dict
supply_trbx_dict = supply_trbx_instance.to_dict()
# create an instance of SupplyTrbx from a dict
supply_trbx_from_dict = SupplyTrbx.from_dict(supply_trbx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



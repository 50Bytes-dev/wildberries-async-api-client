# ApiV3SuppliesSupplyIdBarcodeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Закодированное значение этикетки (идентификатор поставки) | [optional] 
**file** | **bytearray** | Полное представление этикетки в заданном формате. (кодировка base64) | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v3_supplies_supply_id_barcode_get200_response import ApiV3SuppliesSupplyIdBarcodeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SuppliesSupplyIdBarcodeGet200Response from a JSON string
api_v3_supplies_supply_id_barcode_get200_response_instance = ApiV3SuppliesSupplyIdBarcodeGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV3SuppliesSupplyIdBarcodeGet200Response.to_json())

# convert the object into a dict
api_v3_supplies_supply_id_barcode_get200_response_dict = api_v3_supplies_supply_id_barcode_get200_response_instance.to_dict()
# create an instance of ApiV3SuppliesSupplyIdBarcodeGet200Response from a dict
api_v3_supplies_supply_id_barcode_get200_response_from_dict = ApiV3SuppliesSupplyIdBarcodeGet200Response.from_dict(api_v3_supplies_supply_id_barcode_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



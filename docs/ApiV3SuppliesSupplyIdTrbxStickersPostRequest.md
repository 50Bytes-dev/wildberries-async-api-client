# ApiV3SuppliesSupplyIdTrbxStickersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trbx_ids** | **List[str]** | Список ID коробов, по которым необходимо вернуть стикеры. | 

## Example

```python
from wildberries_async_api_client.models.api_v3_supplies_supply_id_trbx_stickers_post_request import ApiV3SuppliesSupplyIdTrbxStickersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SuppliesSupplyIdTrbxStickersPostRequest from a JSON string
api_v3_supplies_supply_id_trbx_stickers_post_request_instance = ApiV3SuppliesSupplyIdTrbxStickersPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3SuppliesSupplyIdTrbxStickersPostRequest.to_json())

# convert the object into a dict
api_v3_supplies_supply_id_trbx_stickers_post_request_dict = api_v3_supplies_supply_id_trbx_stickers_post_request_instance.to_dict()
# create an instance of ApiV3SuppliesSupplyIdTrbxStickersPostRequest from a dict
api_v3_supplies_supply_id_trbx_stickers_post_request_from_dict = ApiV3SuppliesSupplyIdTrbxStickersPostRequest.from_dict(api_v3_supplies_supply_id_trbx_stickers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



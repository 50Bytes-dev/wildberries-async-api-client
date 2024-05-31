# TrbxStickers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Закодированное значение этикетки. | [optional] 
**file** | **bytearray** | Полное представление этикетки в заданном формате. (кодировка base64) | [optional] 

## Example

```python
from wb_client.models.trbx_stickers import TrbxStickers

# TODO update the JSON string below
json = "{}"
# create an instance of TrbxStickers from a JSON string
trbx_stickers_instance = TrbxStickers.from_json(json)
# print the JSON string representation of the object
print(TrbxStickers.to_json())

# convert the object into a dict
trbx_stickers_dict = trbx_stickers_instance.to_dict()
# create an instance of TrbxStickers from a dict
trbx_stickers_from_dict = TrbxStickers.from_dict(trbx_stickers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



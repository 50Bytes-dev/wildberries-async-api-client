# ApiV2ListGoodsSizeNmGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list_goods** | [**List[SizeGood]**](SizeGood.md) | Размеры товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_list_goods_size_nm_get200_response_data import ApiV2ListGoodsSizeNmGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2ListGoodsSizeNmGet200ResponseData from a JSON string
api_v2_list_goods_size_nm_get200_response_data_instance = ApiV2ListGoodsSizeNmGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV2ListGoodsSizeNmGet200ResponseData.to_json())

# convert the object into a dict
api_v2_list_goods_size_nm_get200_response_data_dict = api_v2_list_goods_size_nm_get200_response_data_instance.to_dict()
# create an instance of ApiV2ListGoodsSizeNmGet200ResponseData from a dict
api_v2_list_goods_size_nm_get200_response_data_from_dict = ApiV2ListGoodsSizeNmGet200ResponseData.from_dict(api_v2_list_goods_size_nm_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



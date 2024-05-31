# GoodsList

Размеры товара

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**sizes** | [**List[GoodsListSizesInner]**](GoodsListSizesInner.md) | Размер | [optional] 
**currency_iso_code4217** | **str** | Валюта, по стандарту ISO 4217 | [optional] 
**discount** | **int** | Скидка, % | [optional] 
**editable_size_price** | **bool** | Можно ли устанавливать цены отдельно для разных размеров: &#x60;true&#x60; — можно, &#x60;false&#x60; — нельзя. Эта возможность зависит от категории товара  | [optional] 

## Example

```python
from wildberries_async_api_client.models.goods_list import GoodsList

# TODO update the JSON string below
json = "{}"
# create an instance of GoodsList from a JSON string
goods_list_instance = GoodsList.from_json(json)
# print the JSON string representation of the object
print(GoodsList.to_json())

# convert the object into a dict
goods_list_dict = goods_list_instance.to_dict()
# create an instance of GoodsList from a dict
goods_list_from_dict = GoodsList.from_dict(goods_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



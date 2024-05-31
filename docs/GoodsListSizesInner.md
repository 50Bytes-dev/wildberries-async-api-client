# GoodsListSizesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_id** | **int** | ID размера. В методах контента это поле &#x60;chrtID&#x60; | [optional] 
**price** | **int** | Цена | [optional] 
**discounted_price** | **float** | Цена со скидкой | [optional] 
**tech_size_name** | **str** | Размер товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.goods_list_sizes_inner import GoodsListSizesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GoodsListSizesInner from a JSON string
goods_list_sizes_inner_instance = GoodsListSizesInner.from_json(json)
# print the JSON string representation of the object
print(GoodsListSizesInner.to_json())

# convert the object into a dict
goods_list_sizes_inner_dict = goods_list_sizes_inner_instance.to_dict()
# create an instance of GoodsListSizesInner from a dict
goods_list_sizes_inner_from_dict = GoodsListSizesInner.from_dict(goods_list_sizes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



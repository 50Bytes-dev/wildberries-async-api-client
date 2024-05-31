# SizeGood

Информация о размере

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | [optional] 
**size_id** | **int** | ID размера. Можно получить с помощью метода [Получение списка товаров по артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), поле &#x60;sizeID&#x60;. В методах контента это поле &#x60;chrtID&#x60; | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**price** | **int** | Цена | [optional] 
**currency_iso_code4217** | **str** | Валюта, по стандарту ISO 4217 | [optional] 
**discounted_price** | **float** | Цена со скидкой | [optional] 
**discount** | **int** | Скидка, % | [optional] 
**tech_size_name** | **str** | Размер товара | [optional] 
**editable_size_price** | **bool** | Можно ли устанавливать цены отдельно для разных размеров: &#x60;true&#x60; — можно, &#x60;false&#x60; — нельзя. Эта возможность зависит от категории товара  | [optional] 

## Example

```python
from wildberries_async_api_client.models.size_good import SizeGood

# TODO update the JSON string below
json = "{}"
# create an instance of SizeGood from a JSON string
size_good_instance = SizeGood.from_json(json)
# print the JSON string representation of the object
print(SizeGood.to_json())

# convert the object into a dict
size_good_dict = size_good_instance.to_dict()
# create an instance of SizeGood from a dict
size_good_from_dict = SizeGood.from_dict(size_good_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



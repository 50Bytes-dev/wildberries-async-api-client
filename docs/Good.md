# Good


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | 
**price** | **int** | Цена. Валюту можно получить с помощью метода [Получение списка товаров по артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), поле &#x60;currencyIsoCode4217&#x60; | [optional] 
**discount** | **int** | Скидка, % | [optional] 

## Example

```python
from wildberries_async_api_client.models.good import Good

# TODO update the JSON string below
json = "{}"
# create an instance of Good from a JSON string
good_instance = Good.from_json(json)
# print the JSON string representation of the object
print(Good.to_json())

# convert the object into a dict
good_dict = good_instance.to_dict()
# create an instance of Good from a dict
good_from_dict = Good.from_dict(good_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



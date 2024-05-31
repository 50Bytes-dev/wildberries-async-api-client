# SizeGoodReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | 
**size_id** | **int** | ID размера. Можно получить с помощью метода [Получение списка товаров по артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), поле &#x60;sizeID&#x60;. В методах контента это поле &#x60;chrtID&#x60; | 
**price** | **int** | Цена. Валюту можно получить с помощью метода [Получение списка товаров по артикулам](./#tag/Spiski-tovarov/paths/~1api~1v2~1list~1goods~1filter/get), поле &#x60;currencyIsoCode4217&#x60; | 

## Example

```python
from wildberries_async_api_client.models.size_good_req import SizeGoodReq

# TODO update the JSON string below
json = "{}"
# create an instance of SizeGoodReq from a JSON string
size_good_req_instance = SizeGoodReq.from_json(json)
# print the JSON string representation of the object
print(SizeGoodReq.to_json())

# convert the object into a dict
size_good_req_dict = size_good_req_instance.to_dict()
# create an instance of SizeGoodReq from a dict
size_good_req_from_dict = SizeGoodReq.from_dict(size_good_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



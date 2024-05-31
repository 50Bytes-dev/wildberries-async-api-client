# GoodHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул Wildberries | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**size_id** | **int** | ID размера. В методах контента это поле &#x60;chrtID&#x60; | [optional] 
**tech_size_name** | **str** | Размер | [optional] 
**price** | **int** | Цена | [optional] 
**currency_iso_code4217** | **str** | Валюта, по стандарту ISO 4217 | [optional] 
**discount** | **int** | Скидка, % | [optional] 
**status** | **int** | Статус товара:    * &#x60;2&#x60; — товар без ошибок, цена и/или скидка обновилась   * &#x60;3&#x60; — есть ошибки, данные не обновились  | [optional] 
**error_text** | **str** | Текст ошибки  &lt;blockquote class&#x3D;\&quot;spoiler\&quot;&gt;   &lt;p class&#x3D;\&quot;descr\&quot;&gt;Ошибка &lt;code&gt;The product is in quarantine&lt;/code&gt; возникает, если новая цена со скидкой хотя бы в 3 раза меньше старой. Вы можете изменить цену или скидку с помощью API либо вывести товар из карантина &lt;a href&#x3D;\&quot;https://seller.wildberries.ru/discount-and-prices/quarantine\&quot;&gt;в личном кабинете&lt;/a&gt;&lt;/p&gt; &lt;/blockquote&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.good_history import GoodHistory

# TODO update the JSON string below
json = "{}"
# create an instance of GoodHistory from a JSON string
good_history_instance = GoodHistory.from_json(json)
# print the JSON string representation of the object
print(GoodHistory.to_json())

# convert the object into a dict
good_history_dict = good_history_instance.to_dict()
# create an instance of GoodHistory from a dict
good_history_from_dict = GoodHistory.from_dict(good_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



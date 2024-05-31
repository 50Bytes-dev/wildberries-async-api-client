# AdvV1SaveAdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип автоматической кампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;8&lt;/code&gt; &lt;/dl&gt;  | [optional] 
**name** | **str** | Название кампании (max. 128 символов) | [optional] 
**subject_id** | **int** | ID предмета, для которого создается кампания.&lt;br&gt; Существующие у продавца идентификаторы можно получить методом из раздела \&quot;Контент / Просмотр\&quot; - \&quot;Список НМ\&quot;, поле ответа - &#x60;objectID&#x60;.  | [optional] 
**sum** | **int** | Сумма пополнения | [optional] 
**btype** | **int** | &lt;dl&gt; &lt;dt&gt;Tип списания.&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;0&lt;/code&gt; - Счёт&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - Баланс&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;3&lt;/code&gt; - Бонусы&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**on_pause** | **bool** | &lt;dl&gt; &lt;dt&gt;После создания кампания:&lt;/dt&gt;  &lt;dd&gt;   &lt;dl&gt;     &lt;dt&gt;&lt;code&gt;true&lt;/code&gt; - будет на паузе.&lt;/dt&gt;     &lt;dd&gt;Запуск кампании будет доступен через 3 минуты после создания кампании.&lt;/dd&gt;   &lt;/dl&gt; &lt;/dd&gt;  &lt;dd&gt;&lt;code&gt;false&lt;/code&gt; - будет сразу запущена&lt;/dd&gt;  &lt;/dl&gt;  | [optional] 
**nms** | **List[int]** | Массив артикулов WB. &lt;br&gt; Максимум 100 артикулов.   | [optional] 
**cpm** | **int** | Ставка. &lt;br&gt; Если будет указана ставка меньше допустимого размера, то автоматически установится ставка минимально допустимого размера.  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_save_ad_post_request import AdvV1SaveAdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1SaveAdPostRequest from a JSON string
adv_v1_save_ad_post_request_instance = AdvV1SaveAdPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1SaveAdPostRequest.to_json())

# convert the object into a dict
adv_v1_save_ad_post_request_dict = adv_v1_save_ad_post_request_instance.to_dict()
# create an instance of AdvV1SaveAdPostRequest from a dict
adv_v1_save_ad_post_request_from_dict = AdvV1SaveAdPostRequest.from_dict(adv_v1_save_ad_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



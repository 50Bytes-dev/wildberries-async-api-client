# AdvV1AdvertGet200ResponseItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID баннера | [optional] 
**name** | **str** | Бренд | [optional] 
**status** | **int** | Статус (такой же как у медиакампании) | [optional] 
**place** | **int** | Позиция на странице размещения | [optional] 
**budget** | **int** | Бюджет | [optional] 
**daily_limit** | **int** | Дневной лимит (для баннеров по показам) | [optional] 
**category_name** | **str** | Название категории размещения | [optional] 
**cpm** | **int** | Ставка | [optional] 
**url** | **str** | URL страницы, на которую попадает пользователь при клике по баннеру | [optional] 
**advert_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип продвижения:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - баннер&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;2&lt;/code&gt; - всплывающее меню&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;3&lt;/code&gt; - почтовая рассылка&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;4&lt;/code&gt; - социальные сети&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;5&lt;/code&gt; - push-уведомления в мобильном приложении&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**created_at** | **datetime** | Дата создания баннера | [optional] 
**updated_at** | **datetime** | Дата обновления баннера | [optional] 
**date_from** | **datetime** | Дата начала работы баннера | [optional] 
**date_to** | **datetime** | Дата завершения работы баннера | [optional] 
**nms** | **List[int]** | Подборка артикулов WB | [optional] 
**bottom_text1** | **str** | Текст под плашкой баннера | [optional] 
**bottom_text2** | **str** | 2-я строка с текстом под плашкой баннера | [optional] 
**message** | **str** | Текст push-уведомления или рассылки | [optional] 
**additional_settings** | **int** | Дополнительные настройки. &lt;dl&gt; &lt;dt&gt;Формат почтовой рассылки:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - общий&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;2&lt;/code&gt; - частичный&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;3&lt;/code&gt; - уникальный&lt;/dd&gt; &lt;/dl&gt; &lt;dl&gt; &lt;dt&gt;Социальная сеть:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - VKontakte&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;2&lt;/code&gt; - OK (Одноклассники)&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**receivers_count** | **int** | Кол-во получателей push-уведомлений | [optional] 
**subject_id** | **int** | ID родительской категории товара | [optional] 
**subject_name** | **str** | Название родительской категории товара | [optional] 
**action_name** | **str** | Название акции | [optional] 
**show_hours** | [**List[AdvV1AdvertGet200ResponseItemsInnerShowHoursInner]**](AdvV1AdvertGet200ResponseItemsInnerShowHoursInner.md) | Часы показа | [optional] 
**erid** | **str** | Уникальный идентификатор медиакампании для работы с ОРД | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_advert_get200_response_items_inner import AdvV1AdvertGet200ResponseItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AdvertGet200ResponseItemsInner from a JSON string
adv_v1_advert_get200_response_items_inner_instance = AdvV1AdvertGet200ResponseItemsInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1AdvertGet200ResponseItemsInner.to_json())

# convert the object into a dict
adv_v1_advert_get200_response_items_inner_dict = adv_v1_advert_get200_response_items_inner_instance.to_dict()
# create an instance of AdvV1AdvertGet200ResponseItemsInner from a dict
adv_v1_advert_get200_response_items_inner_from_dict = AdvV1AdvertGet200ResponseItemsInner.from_dict(adv_v1_advert_get200_response_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



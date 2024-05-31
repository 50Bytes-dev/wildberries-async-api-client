# StatsBlok1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **int** | ID баннера | [optional] 
**item_name** | **str** | Название бренда | [optional] 
**category_name** | **str** | Название категории | [optional] 
**advert_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип медиакампании:&lt;/dt&gt; &lt;dd&gt;&lt;code&gt;1&lt;/code&gt; - размещение по дням&lt;/dd&gt; &lt;dd&gt;&lt;code&gt;2&lt;/code&gt; - размещение по просмотрам&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**place** | **int** | Место на странице | [optional] 
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **int** | Количество кликов | [optional] 
**cr** | **float** | CR(conversion rate) — это отношение количества заказов к общему количеству посещений медиакампании  | [optional] 
**ctr** | **float** | CTR (click-through rate) — показатель кликабельности, отношение числа кликов к количеству показов в рамках медиакампании  | [optional] 
**date_from** | **datetime** | Время начала размещения | [optional] 
**date_to** | **datetime** | Время завершения размещения | [optional] 
**subject_name** | **str** | Родительская категория предмета | [optional] 
**atbs** | **int** | Количество добавлений товаров в корзину | [optional] 
**orders** | **int** | Количество заказов | [optional] 
**price** | **int** | Стоимость размещения | [optional] 
**cpc** | **float** | (cost per click) - цена клика по продвигаемому товару | [optional] 
**status** | **int** | Статус медиакампании | [optional] 
**daily_stats** | [**List[DailyStats1Inner]**](DailyStats1Inner.md) |  | [optional] 
**expenses** | **int** | Стоимость размещения баннера | [optional] 
**cr1** | **float** | Отношение количества добавлений в корзину к количеству кликов | [optional] 
**cr2** | **int** | Отношение количества заказов к количеству добавлений в корзину | [optional] 

## Example

```python
from wildberries_async_api_client.models.stats_blok1 import StatsBlok1

# TODO update the JSON string below
json = "{}"
# create an instance of StatsBlok1 from a JSON string
stats_blok1_instance = StatsBlok1.from_json(json)
# print the JSON string representation of the object
print(StatsBlok1.to_json())

# convert the object into a dict
stats_blok1_dict = stats_blok1_instance.to_dict()
# create an instance of StatsBlok1 from a dict
stats_blok1_from_dict = StatsBlok1.from_dict(stats_blok1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



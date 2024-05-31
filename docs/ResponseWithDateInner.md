# ResponseWithDateInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | **List[date]** | Даты, за которые необходимо выдать информацию. | [optional] 
**views** | **int** | Количество просмотров. &lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**clicks** | **int** | Количество кликов.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**ctr** | **float** | Показатель кликабельности.&lt;br&gt; Отношение числа кликов к количеству показов. Выражается в процентах.&lt;br&gt; За все дни, по всем артикулам WB и платформам.&lt;br&gt;  | [optional] 
**cpc** | **float** | Средняя стоимость клика, ₽.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**sum** | **float** | Затраты, ₽.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**atbs** | **int** | Количество добавлений товаров в корзину.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**orders** | **int** | Количество заказов.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**cr** | **int** | CR(conversion rate) — это отношение количества заказов к общему количеству посещений кампании.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**shks** | **int** | Количество заказанных товаров, шт.&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**sum_price** | **float** | Заказов на сумму, ₽&lt;br&gt; За все дни, по всем артикулам WB и платформам.  | [optional] 
**days** | [**List[DaysInner]**](DaysInner.md) | Статистка по дням | [optional] 
**booster_stats** | [**List[BoosterStatsInner]**](BoosterStatsInner.md) | Статистика по средней позиции товара на страницах поисковой выдачи и каталога (для автоматических кампаний). | [optional] 
**advert_id** | **int** | ID кампании | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_with_date_inner import ResponseWithDateInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseWithDateInner from a JSON string
response_with_date_inner_instance = ResponseWithDateInner.from_json(json)
# print the JSON string representation of the object
print(ResponseWithDateInner.to_json())

# convert the object into a dict
response_with_date_inner_dict = response_with_date_inner_instance.to_dict()
# create an instance of ResponseWithDateInner from a dict
response_with_date_inner_from_dict = ResponseWithDateInner.from_dict(response_with_date_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



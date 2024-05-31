# DaysInnerAppsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **int** | Количество кликов | [optional] 
**ctr** | **float** | Показатель кликабельности, отношение числа кликов к количеству показов, %  | [optional] 
**cpc** | **float** | Средняя стоимость клика, ₽. | [optional] 
**sum** | **float** | Затраты, ₽. | [optional] 
**atbs** | **int** | Количество добавлений товаров в корзину | [optional] 
**orders** | **int** | Количество заказов | [optional] 
**cr** | **int** | CR(conversion rate) — это отношение количества заказов к общему количеству посещений кампании  | [optional] 
**shks** | **int** | Количество заказанных товаров, шт. | [optional] 
**sum_price** | **float** | Заказов на сумму, ₽ | [optional] 
**nm** | [**List[DaysInnerAppsInnerNmInner]**](DaysInnerAppsInnerNmInner.md) | Блок статистики по артикулам WB | [optional] 
**app_type** | **int** | Тип платформы (&#x60;1&#x60; - сайт, &#x60;32&#x60; - Android, &#x60;64&#x60; - IOS) | [optional] 

## Example

```python
from wildberries_async_api_client.models.days_inner_apps_inner import DaysInnerAppsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DaysInnerAppsInner from a JSON string
days_inner_apps_inner_instance = DaysInnerAppsInner.from_json(json)
# print the JSON string representation of the object
print(DaysInnerAppsInner.to_json())

# convert the object into a dict
days_inner_apps_inner_dict = days_inner_apps_inner_instance.to_dict()
# create an instance of DaysInnerAppsInner from a dict
days_inner_apps_inner_from_dict = DaysInnerAppsInner.from_dict(days_inner_apps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



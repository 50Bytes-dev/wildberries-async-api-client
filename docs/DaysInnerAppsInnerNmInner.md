# DaysInnerAppsInnerNmInner


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
**cr** | **int** | CR(conversion rate) — отношение количества заказов к общему количеству посещений кампании  | [optional] 
**shks** | **int** | Количество заказанных товаров, шт. | [optional] 
**sum_price** | **float** | Заказов на сумму, ₽ | [optional] 
**name** | **str** |  | [optional] 
**nm_id** | **int** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.days_inner_apps_inner_nm_inner import DaysInnerAppsInnerNmInner

# TODO update the JSON string below
json = "{}"
# create an instance of DaysInnerAppsInnerNmInner from a JSON string
days_inner_apps_inner_nm_inner_instance = DaysInnerAppsInnerNmInner.from_json(json)
# print the JSON string representation of the object
print(DaysInnerAppsInnerNmInner.to_json())

# convert the object into a dict
days_inner_apps_inner_nm_inner_dict = days_inner_apps_inner_nm_inner_instance.to_dict()
# create an instance of DaysInnerAppsInnerNmInner from a dict
days_inner_apps_inner_nm_inner_from_dict = DaysInnerAppsInnerNmInner.from_dict(days_inner_apps_inner_nm_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Stats2Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **int** | Количество кликов | [optional] 
**atbs** | **int** | Количество добавлений товаров в корзину | [optional] 
**orders** | **int** | Количество заказов | [optional] 
**cr** | **float** | CR(conversion rate) — отношение количества заказов к общему количеству посещений медиакампании                | [optional] 
**ctr** | **float** | CTR (click-through rate) — показатель кликабельности, отношение числа кликов к количеству показов в рамках медиакампании  | [optional] 

## Example

```python
from wildberries_async_api_client.models.stats2_inner import Stats2Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Stats2Inner from a JSON string
stats2_inner_instance = Stats2Inner.from_json(json)
# print the JSON string representation of the object
print(Stats2Inner.to_json())

# convert the object into a dict
stats2_inner_dict = stats2_inner_instance.to_dict()
# create an instance of Stats2Inner from a dict
stats2_inner_from_dict = Stats2Inner.from_dict(stats2_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



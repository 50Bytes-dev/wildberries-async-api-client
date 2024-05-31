# Stats1Inner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **int** | Количество кликов | [optional] 
**atbs** | **int** | Количество добавлений товаров в корзину | [optional] 
**ctr** | **float** | CTR (click-through rate) — показатель кликабельности, отношение числа кликов к количеству показов в рамках медиакампании                | [optional] 

## Example

```python
from wildberries_async_api_client.models.stats1_inner import Stats1Inner

# TODO update the JSON string below
json = "{}"
# create an instance of Stats1Inner from a JSON string
stats1_inner_instance = Stats1Inner.from_json(json)
# print the JSON string representation of the object
print(Stats1Inner.to_json())

# convert the object into a dict
stats1_inner_dict = stats1_inner_instance.to_dict()
# create an instance of Stats1Inner from a dict
stats1_inner_from_dict = Stats1Inner.from_dict(stats1_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



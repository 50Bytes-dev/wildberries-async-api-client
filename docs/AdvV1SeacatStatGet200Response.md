# AdvV1SeacatStatGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_views** | **int** | Суммарное количество просмотров | [optional] 
**total_clicks** | **int** | Суммарное количество кликов | [optional] 
**total_orders** | **int** | Суммарное количество заказов | [optional] 
**total_sum** | **int** | Суммарные затраты, ₽. | [optional] 
**dates** | [**List[AdvV1SeacatStatGet200ResponseDatesInner]**](AdvV1SeacatStatGet200ResponseDatesInner.md) | Блок статистики | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_seacat_stat_get200_response import AdvV1SeacatStatGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1SeacatStatGet200Response from a JSON string
adv_v1_seacat_stat_get200_response_instance = AdvV1SeacatStatGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV1SeacatStatGet200Response.to_json())

# convert the object into a dict
adv_v1_seacat_stat_get200_response_dict = adv_v1_seacat_stat_get200_response_instance.to_dict()
# create an instance of AdvV1SeacatStatGet200Response from a dict
adv_v1_seacat_stat_get200_response_from_dict = AdvV1SeacatStatGet200Response.from_dict(adv_v1_seacat_stat_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV1AutoStatGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**views** | **int** | Количество просмотров | [optional] 
**clicks** | **float** | Количество кликов | [optional] 
**ctr** | **float** | CTR (Click-Through Rate) — показатель кликабельности. &lt;br&gt; Отношение числа кликов к количеству показов. Выражается в процентах.  | [optional] 
**cpc** | **float** | CPC(от англ. cost per click — цена за клик) — это цена клика по продвигаемому товару. | [optional] 
**spend** | **int** | Затраты, ₽. | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_auto_stat_get200_response import AdvV1AutoStatGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AutoStatGet200Response from a JSON string
adv_v1_auto_stat_get200_response_instance = AdvV1AutoStatGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV1AutoStatGet200Response.to_json())

# convert the object into a dict
adv_v1_auto_stat_get200_response_dict = adv_v1_auto_stat_get200_response_instance.to_dict()
# create an instance of AdvV1AutoStatGet200Response from a dict
adv_v1_auto_stat_get200_response_from_dict = AdvV1AutoStatGet200Response.from_dict(adv_v1_auto_stat_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



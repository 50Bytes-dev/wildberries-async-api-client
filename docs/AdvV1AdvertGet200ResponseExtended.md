# AdvV1AdvertGet200ResponseExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Комментарий модератора (при наличии) | [optional] 
**expenses** | **int** | Затраты | [optional] 
**var_from** | **datetime** | Начало показов медиакампании | [optional] 
**to** | **datetime** | Конец показов медиакампании | [optional] 
**updated_at** | **datetime** | Время изменения медиакампании | [optional] 
**price** | **int** | Стоимость размещения по дням (для типа 1) | [optional] 
**budget** | **int** | Остаток бюджета (для типа 2) | [optional] 
**operation** | **int** | Источник списания (1 - баланс, 2 - счет) | [optional] 
**contract_id** | **int** | Идентификатор контракта (для продавцов на контракте) | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_advert_get200_response_extended import AdvV1AdvertGet200ResponseExtended

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AdvertGet200ResponseExtended from a JSON string
adv_v1_advert_get200_response_extended_instance = AdvV1AdvertGet200ResponseExtended.from_json(json)
# print the JSON string representation of the object
print(AdvV1AdvertGet200ResponseExtended.to_json())

# convert the object into a dict
adv_v1_advert_get200_response_extended_dict = adv_v1_advert_get200_response_extended_instance.to_dict()
# create an instance of AdvV1AdvertGet200ResponseExtended from a dict
adv_v1_advert_get200_response_extended_from_dict = AdvV1AdvertGet200ResponseExtended.from_dict(adv_v1_advert_get200_response_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



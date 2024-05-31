# AdvV1PromotionCountGet200ResponseAdvertsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | Тип кампании | [optional] 
**status** | **int** | Статус кампании | [optional] 
**count** | **int** | Количество кампаний | [optional] 
**advert_list** | [**List[AdvV1PromotionCountGet200ResponseAdvertsInnerAdvertListInner]**](AdvV1PromotionCountGet200ResponseAdvertsInnerAdvertListInner.md) | Список кампаний | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_promotion_count_get200_response_adverts_inner import AdvV1PromotionCountGet200ResponseAdvertsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1PromotionCountGet200ResponseAdvertsInner from a JSON string
adv_v1_promotion_count_get200_response_adverts_inner_instance = AdvV1PromotionCountGet200ResponseAdvertsInner.from_json(json)
# print the JSON string representation of the object
print(AdvV1PromotionCountGet200ResponseAdvertsInner.to_json())

# convert the object into a dict
adv_v1_promotion_count_get200_response_adverts_inner_dict = adv_v1_promotion_count_get200_response_adverts_inner_instance.to_dict()
# create an instance of AdvV1PromotionCountGet200ResponseAdvertsInner from a dict
adv_v1_promotion_count_get200_response_adverts_inner_from_dict = AdvV1PromotionCountGet200ResponseAdvertsInner.from_dict(adv_v1_promotion_count_get200_response_adverts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



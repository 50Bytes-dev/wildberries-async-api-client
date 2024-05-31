# ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор характеристики | [optional] 
**name** | **str** | Название характеристики | [optional] 
**value** | **object** | Значение характеристики. Тип значения зависит от типа характеристики | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response_cards_inner_characteristics_inner import ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner from a JSON string
content_v2_get_cards_list_post200_response_cards_inner_characteristics_inner_instance = ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner.to_json())

# convert the object into a dict
content_v2_get_cards_list_post200_response_cards_inner_characteristics_inner_dict = content_v2_get_cards_list_post200_response_cards_inner_characteristics_inner_instance.to_dict()
# create an instance of ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner from a dict
content_v2_get_cards_list_post200_response_cards_inner_characteristics_inner_from_dict = ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner.from_dict(content_v2_get_cards_list_post200_response_cards_inner_characteristics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



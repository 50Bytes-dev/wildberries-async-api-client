# ContentV2CardsUpdatePostRequestInnerCharacteristicsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID характеристики | [optional] 
**value** | **object** | Значение характеристики. Тип значения зависит от типа характеристики. | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_update_post_request_inner_characteristics_inner import ContentV2CardsUpdatePostRequestInnerCharacteristicsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUpdatePostRequestInnerCharacteristicsInner from a JSON string
content_v2_cards_update_post_request_inner_characteristics_inner_instance = ContentV2CardsUpdatePostRequestInnerCharacteristicsInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUpdatePostRequestInnerCharacteristicsInner.to_json())

# convert the object into a dict
content_v2_cards_update_post_request_inner_characteristics_inner_dict = content_v2_cards_update_post_request_inner_characteristics_inner_instance.to_dict()
# create an instance of ContentV2CardsUpdatePostRequestInnerCharacteristicsInner from a dict
content_v2_cards_update_post_request_inner_characteristics_inner_from_dict = ContentV2CardsUpdatePostRequestInnerCharacteristicsInner.from_dict(content_v2_cards_update_post_request_inner_characteristics_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



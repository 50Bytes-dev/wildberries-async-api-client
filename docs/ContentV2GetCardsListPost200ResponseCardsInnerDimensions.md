# ContentV2GetCardsListPost200ResponseCardsInnerDimensions

Габариты упаковки товара, см

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Длина, см | [optional] 
**width** | **int** | Ширина, см | [optional] 
**height** | **int** | Высота, см | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response_cards_inner_dimensions import ContentV2GetCardsListPost200ResponseCardsInnerDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPost200ResponseCardsInnerDimensions from a JSON string
content_v2_get_cards_list_post200_response_cards_inner_dimensions_instance = ContentV2GetCardsListPost200ResponseCardsInnerDimensions.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPost200ResponseCardsInnerDimensions.to_json())

# convert the object into a dict
content_v2_get_cards_list_post200_response_cards_inner_dimensions_dict = content_v2_get_cards_list_post200_response_cards_inner_dimensions_instance.to_dict()
# create an instance of ContentV2GetCardsListPost200ResponseCardsInnerDimensions from a dict
content_v2_get_cards_list_post200_response_cards_inner_dimensions_from_dict = ContentV2GetCardsListPost200ResponseCardsInnerDimensions.from_dict(content_v2_get_cards_list_post200_response_cards_inner_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



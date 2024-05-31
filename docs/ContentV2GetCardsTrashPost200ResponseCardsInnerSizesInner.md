# ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chrt_id** | **int** | ID размера | [optional] 
**tech_size** | **str** | Размер товара | [optional] 
**wb_size** | **str** | Российский размер товара | [optional] 
**skus** | **List[str]** | Массив баркодов | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_trash_post200_response_cards_inner_sizes_inner import ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner from a JSON string
content_v2_get_cards_trash_post200_response_cards_inner_sizes_inner_instance = ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner.to_json())

# convert the object into a dict
content_v2_get_cards_trash_post200_response_cards_inner_sizes_inner_dict = content_v2_get_cards_trash_post200_response_cards_inner_sizes_inner_instance.to_dict()
# create an instance of ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner from a dict
content_v2_get_cards_trash_post200_response_cards_inner_sizes_inner_from_dict = ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner.from_dict(content_v2_get_cards_trash_post200_response_cards_inner_sizes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



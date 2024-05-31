# ContentV2GetCardsTrashPost200ResponseCardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**subject_id** | **str** | Идентификатор предмета | [optional] 
**subject_name** | **str** | Название предмета | [optional] 
**photos** | [**List[ContentV2GetCardsListPost200ResponseCardsInnerPhotosInner]**](ContentV2GetCardsListPost200ResponseCardsInnerPhotosInner.md) | Массив фото | [optional] 
**video** | **str** | URL видео | [optional] 
**sizes** | [**List[ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner]**](ContentV2GetCardsTrashPost200ResponseCardsInnerSizesInner.md) | Массив размеров | [optional] 
**dimensions** | [**ContentV2GetCardsTrashPost200ResponseCardsInnerDimensions**](ContentV2GetCardsTrashPost200ResponseCardsInnerDimensions.md) |  | [optional] 
**characteristics** | [**List[ContentV2GetCardsTrashPost200ResponseCardsInnerCharacteristicsInner]**](ContentV2GetCardsTrashPost200ResponseCardsInnerCharacteristicsInner.md) | Массив характеристик, при наличии | [optional] 
**created_at** | **str** |  | [optional] 
**trashed_at** | **str** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_trash_post200_response_cards_inner import ContentV2GetCardsTrashPost200ResponseCardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsTrashPost200ResponseCardsInner from a JSON string
content_v2_get_cards_trash_post200_response_cards_inner_instance = ContentV2GetCardsTrashPost200ResponseCardsInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsTrashPost200ResponseCardsInner.to_json())

# convert the object into a dict
content_v2_get_cards_trash_post200_response_cards_inner_dict = content_v2_get_cards_trash_post200_response_cards_inner_instance.to_dict()
# create an instance of ContentV2GetCardsTrashPost200ResponseCardsInner from a dict
content_v2_get_cards_trash_post200_response_cards_inner_from_dict = ContentV2GetCardsTrashPost200ResponseCardsInner.from_dict(content_v2_get_cards_trash_post200_response_cards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



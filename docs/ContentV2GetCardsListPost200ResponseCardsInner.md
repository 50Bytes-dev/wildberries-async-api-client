# ContentV2GetCardsListPost200ResponseCardsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**imt_id** | **int** | Идентификатор КТ. &lt;br&gt; Артикулы WB из одной КТ будут иметь одинаковый imtID | [optional] 
**nm_uuid** | **str** | Внутренний технический идентификатор товара | [optional] 
**subject_id** | **int** | Идентификатор предмета | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**subject_name** | **str** | Название предмета | [optional] 
**brand** | **str** | Бренд | [optional] 
**title** | **str** | Наименование товара | [optional] 
**photos** | [**List[ContentV2GetCardsListPost200ResponseCardsInnerPhotosInner]**](ContentV2GetCardsListPost200ResponseCardsInnerPhotosInner.md) | Массив фото | [optional] 
**video** | **str** | URL видео | [optional] 
**dimensions** | [**ContentV2GetCardsListPost200ResponseCardsInnerDimensions**](ContentV2GetCardsListPost200ResponseCardsInnerDimensions.md) |  | [optional] 
**characteristics** | [**List[ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner]**](ContentV2GetCardsListPost200ResponseCardsInnerCharacteristicsInner.md) | Характеристики | [optional] 
**sizes** | [**List[ContentV2GetCardsListPost200ResponseCardsInnerSizesInner]**](ContentV2GetCardsListPost200ResponseCardsInnerSizesInner.md) | Размеры товара | [optional] 
**tags** | [**List[ContentV2GetCardsListPost200ResponseCardsInnerTagsInner]**](ContentV2GetCardsListPost200ResponseCardsInnerTagsInner.md) | Теги | [optional] 
**created_at** | **str** | Дата создания | [optional] 
**updated_at** | **str** | Дата изменения | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response_cards_inner import ContentV2GetCardsListPost200ResponseCardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPost200ResponseCardsInner from a JSON string
content_v2_get_cards_list_post200_response_cards_inner_instance = ContentV2GetCardsListPost200ResponseCardsInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPost200ResponseCardsInner.to_json())

# convert the object into a dict
content_v2_get_cards_list_post200_response_cards_inner_dict = content_v2_get_cards_list_post200_response_cards_inner_instance.to_dict()
# create an instance of ContentV2GetCardsListPost200ResponseCardsInner from a dict
content_v2_get_cards_list_post200_response_cards_inner_from_dict = ContentV2GetCardsListPost200ResponseCardsInner.from_dict(content_v2_get_cards_list_post200_response_cards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentV2GetCardsListPostRequestSettingsFilter

Параметры фильтрации

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**with_photo** | **int** | Фильтр по фото:      * &#x60;0&#x60; — только карточки без фото   * &#x60;1&#x60; — только карточки с фото   * &#x60;-1&#x60; — все карточки товара  | [optional] 
**text_search** | **str** | Поиск по артикулу продавца, артикулу WB, баркоду | [optional] 
**tag_ids** | **List[int]** | Поиск по ID тегов | [optional] 
**allowed_categories_only** | **bool** | Фильтр по категории. &#x60;true&#x60; - только разрешённые, &#x60;false&#x60; - все. Не используется в песочнице. | [optional] 
**object_ids** | **List[int]** | Поиск по id предметов | [optional] 
**brands** | **List[str]** | Поиск по брендам | [optional] 
**imt_id** | **int** | Поиск по идентификатору КТ | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post_request_settings_filter import ContentV2GetCardsListPostRequestSettingsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPostRequestSettingsFilter from a JSON string
content_v2_get_cards_list_post_request_settings_filter_instance = ContentV2GetCardsListPostRequestSettingsFilter.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPostRequestSettingsFilter.to_json())

# convert the object into a dict
content_v2_get_cards_list_post_request_settings_filter_dict = content_v2_get_cards_list_post_request_settings_filter_instance.to_dict()
# create an instance of ContentV2GetCardsListPostRequestSettingsFilter from a dict
content_v2_get_cards_list_post_request_settings_filter_from_dict = ContentV2GetCardsListPostRequestSettingsFilter.from_dict(content_v2_get_cards_list_post_request_settings_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentV2GetCardsTrashPostRequestSettingsFilter

Параметры фильтрации

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_search** | **str** | Поиск по артикулу продавца, артикулу WB, баркоду. | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_trash_post_request_settings_filter import ContentV2GetCardsTrashPostRequestSettingsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsTrashPostRequestSettingsFilter from a JSON string
content_v2_get_cards_trash_post_request_settings_filter_instance = ContentV2GetCardsTrashPostRequestSettingsFilter.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsTrashPostRequestSettingsFilter.to_json())

# convert the object into a dict
content_v2_get_cards_trash_post_request_settings_filter_dict = content_v2_get_cards_trash_post_request_settings_filter_instance.to_dict()
# create an instance of ContentV2GetCardsTrashPostRequestSettingsFilter from a dict
content_v2_get_cards_trash_post_request_settings_filter_from_dict = ContentV2GetCardsTrashPostRequestSettingsFilter.from_dict(content_v2_get_cards_trash_post_request_settings_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



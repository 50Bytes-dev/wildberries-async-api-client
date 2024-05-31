# ContentV2GetCardsTrashPostRequestSettings

Настройки

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**ContentV2GetCardsTrashPostRequestSettingsSort**](ContentV2GetCardsTrashPostRequestSettingsSort.md) |  | [optional] 
**cursor** | [**ContentV2GetCardsTrashPostRequestSettingsCursor**](ContentV2GetCardsTrashPostRequestSettingsCursor.md) |  | [optional] 
**filter** | [**ContentV2GetCardsTrashPostRequestSettingsFilter**](ContentV2GetCardsTrashPostRequestSettingsFilter.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_trash_post_request_settings import ContentV2GetCardsTrashPostRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsTrashPostRequestSettings from a JSON string
content_v2_get_cards_trash_post_request_settings_instance = ContentV2GetCardsTrashPostRequestSettings.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsTrashPostRequestSettings.to_json())

# convert the object into a dict
content_v2_get_cards_trash_post_request_settings_dict = content_v2_get_cards_trash_post_request_settings_instance.to_dict()
# create an instance of ContentV2GetCardsTrashPostRequestSettings from a dict
content_v2_get_cards_trash_post_request_settings_from_dict = ContentV2GetCardsTrashPostRequestSettings.from_dict(content_v2_get_cards_trash_post_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



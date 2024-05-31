# ContentV2GetCardsListPostRequestSettings

Настройки

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | [**ContentV2GetCardsListPostRequestSettingsSort**](ContentV2GetCardsListPostRequestSettingsSort.md) |  | [optional] 
**filter** | [**ContentV2GetCardsListPostRequestSettingsFilter**](ContentV2GetCardsListPostRequestSettingsFilter.md) |  | [optional] 
**cursor** | [**ContentV2GetCardsListPostRequestSettingsCursor**](ContentV2GetCardsListPostRequestSettingsCursor.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post_request_settings import ContentV2GetCardsListPostRequestSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPostRequestSettings from a JSON string
content_v2_get_cards_list_post_request_settings_instance = ContentV2GetCardsListPostRequestSettings.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPostRequestSettings.to_json())

# convert the object into a dict
content_v2_get_cards_list_post_request_settings_dict = content_v2_get_cards_list_post_request_settings_instance.to_dict()
# create an instance of ContentV2GetCardsListPostRequestSettings from a dict
content_v2_get_cards_list_post_request_settings_from_dict = ContentV2GetCardsListPostRequestSettings.from_dict(content_v2_get_cards_list_post_request_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentV2GetCardsListPostRequestSettingsSort

Параметр сортировки

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ascending** | **bool** | Сортировать по полю **updatedAt** (&#x60;false&#x60; - по убыванию, &#x60;true&#x60; - по возрастанию) | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post_request_settings_sort import ContentV2GetCardsListPostRequestSettingsSort

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPostRequestSettingsSort from a JSON string
content_v2_get_cards_list_post_request_settings_sort_instance = ContentV2GetCardsListPostRequestSettingsSort.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPostRequestSettingsSort.to_json())

# convert the object into a dict
content_v2_get_cards_list_post_request_settings_sort_dict = content_v2_get_cards_list_post_request_settings_sort_instance.to_dict()
# create an instance of ContentV2GetCardsListPostRequestSettingsSort from a dict
content_v2_get_cards_list_post_request_settings_sort_from_dict = ContentV2GetCardsListPostRequestSettingsSort.from_dict(content_v2_get_cards_list_post_request_settings_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentV2GetCardsListPost200ResponseCursor

Пагинатор

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **str** | Дата с которой надо запрашивать следующий список КТ | [optional] 
**nm_id** | **int** | Номер Артикула WB с которой надо запрашивать следующий список КТ | [optional] 
**total** | **int** | Кол-во возвращенных КТ | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response_cursor import ContentV2GetCardsListPost200ResponseCursor

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPost200ResponseCursor from a JSON string
content_v2_get_cards_list_post200_response_cursor_instance = ContentV2GetCardsListPost200ResponseCursor.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPost200ResponseCursor.to_json())

# convert the object into a dict
content_v2_get_cards_list_post200_response_cursor_dict = content_v2_get_cards_list_post200_response_cursor_instance.to_dict()
# create an instance of ContentV2GetCardsListPost200ResponseCursor from a dict
content_v2_get_cards_list_post200_response_cursor_from_dict = ContentV2GetCardsListPost200ResponseCursor.from_dict(content_v2_get_cards_list_post200_response_cursor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



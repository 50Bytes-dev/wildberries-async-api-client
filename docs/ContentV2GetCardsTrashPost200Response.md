# ContentV2GetCardsTrashPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[ContentV2GetCardsTrashPost200ResponseCardsInner]**](ContentV2GetCardsTrashPost200ResponseCardsInner.md) | Массив карточек товаров | [optional] 
**cursor** | [**ContentV2GetCardsTrashPost200ResponseCursor**](ContentV2GetCardsTrashPost200ResponseCursor.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_trash_post200_response import ContentV2GetCardsTrashPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsTrashPost200Response from a JSON string
content_v2_get_cards_trash_post200_response_instance = ContentV2GetCardsTrashPost200Response.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsTrashPost200Response.to_json())

# convert the object into a dict
content_v2_get_cards_trash_post200_response_dict = content_v2_get_cards_trash_post200_response_instance.to_dict()
# create an instance of ContentV2GetCardsTrashPost200Response from a dict
content_v2_get_cards_trash_post200_response_from_dict = ContentV2GetCardsTrashPost200Response.from_dict(content_v2_get_cards_trash_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



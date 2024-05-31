# ContentV2GetCardsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[ContentV2GetCardsListPost200ResponseCardsInner]**](ContentV2GetCardsListPost200ResponseCardsInner.md) | Список КТ | [optional] 
**cursor** | [**ContentV2GetCardsListPost200ResponseCursor**](ContentV2GetCardsListPost200ResponseCursor.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post200_response import ContentV2GetCardsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPost200Response from a JSON string
content_v2_get_cards_list_post200_response_instance = ContentV2GetCardsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPost200Response.to_json())

# convert the object into a dict
content_v2_get_cards_list_post200_response_dict = content_v2_get_cards_list_post200_response_instance.to_dict()
# create an instance of ContentV2GetCardsListPost200Response from a dict
content_v2_get_cards_list_post200_response_from_dict = ContentV2GetCardsListPost200Response.from_dict(content_v2_get_cards_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



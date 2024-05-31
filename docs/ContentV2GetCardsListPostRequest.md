# ContentV2GetCardsListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**ContentV2GetCardsListPostRequestSettings**](ContentV2GetCardsListPostRequestSettings.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_get_cards_list_post_request import ContentV2GetCardsListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2GetCardsListPostRequest from a JSON string
content_v2_get_cards_list_post_request_instance = ContentV2GetCardsListPostRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV2GetCardsListPostRequest.to_json())

# convert the object into a dict
content_v2_get_cards_list_post_request_dict = content_v2_get_cards_list_post_request_instance.to_dict()
# create an instance of ContentV2GetCardsListPostRequest from a dict
content_v2_get_cards_list_post_request_from_dict = ContentV2GetCardsListPostRequest.from_dict(content_v2_get_cards_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



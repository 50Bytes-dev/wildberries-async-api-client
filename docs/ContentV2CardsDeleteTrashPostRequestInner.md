# ContentV2CardsDeleteTrashPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_ids** | **List[int]** | Артикул WB (max. 1000) | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_delete_trash_post_request_inner import ContentV2CardsDeleteTrashPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsDeleteTrashPostRequestInner from a JSON string
content_v2_cards_delete_trash_post_request_inner_instance = ContentV2CardsDeleteTrashPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsDeleteTrashPostRequestInner.to_json())

# convert the object into a dict
content_v2_cards_delete_trash_post_request_inner_dict = content_v2_cards_delete_trash_post_request_inner_instance.to_dict()
# create an instance of ContentV2CardsDeleteTrashPostRequestInner from a dict
content_v2_cards_delete_trash_post_request_inner_from_dict = ContentV2CardsDeleteTrashPostRequestInner.from_dict(content_v2_cards_delete_trash_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



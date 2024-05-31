# ContentV2CardsRecoverPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_ids** | **int** | Артикул WB (max. 1000) | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_recover_post_request_inner import ContentV2CardsRecoverPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsRecoverPostRequestInner from a JSON string
content_v2_cards_recover_post_request_inner_instance = ContentV2CardsRecoverPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsRecoverPostRequestInner.to_json())

# convert the object into a dict
content_v2_cards_recover_post_request_inner_dict = content_v2_cards_recover_post_request_inner_instance.to_dict()
# create an instance of ContentV2CardsRecoverPostRequestInner from a dict
content_v2_cards_recover_post_request_inner_from_dict = ContentV2CardsRecoverPostRequestInner.from_dict(content_v2_cards_recover_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



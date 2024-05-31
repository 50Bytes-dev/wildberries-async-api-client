# ContentV2CardsUploadAddPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imt_id** | **int** | imtID КТ, к которой добавляется НМ | [optional] 
**cards_to_add** | [**List[ContentV2CardsUploadAddPostRequestCardsToAddInner]**](ContentV2CardsUploadAddPostRequestCardsToAddInner.md) | Структура добавляемой НМ | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_add_post_request import ContentV2CardsUploadAddPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadAddPostRequest from a JSON string
content_v2_cards_upload_add_post_request_instance = ContentV2CardsUploadAddPostRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadAddPostRequest.to_json())

# convert the object into a dict
content_v2_cards_upload_add_post_request_dict = content_v2_cards_upload_add_post_request_instance.to_dict()
# create an instance of ContentV2CardsUploadAddPostRequest from a dict
content_v2_cards_upload_add_post_request_from_dict = ContentV2CardsUploadAddPostRequest.from_dict(content_v2_cards_upload_add_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



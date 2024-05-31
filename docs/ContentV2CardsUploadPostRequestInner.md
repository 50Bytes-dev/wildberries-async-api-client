# ContentV2CardsUploadPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_id** | **int** | ID предмета | 
**variants** | [**List[ContentV2CardsUploadPostRequestInnerVariantsInner]**](ContentV2CardsUploadPostRequestInnerVariantsInner.md) | Массив вариантов товара. В каждой КТ может быть не более 30 вариантов (НМ) | 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_post_request_inner import ContentV2CardsUploadPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadPostRequestInner from a JSON string
content_v2_cards_upload_post_request_inner_instance = ContentV2CardsUploadPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadPostRequestInner.to_json())

# convert the object into a dict
content_v2_cards_upload_post_request_inner_dict = content_v2_cards_upload_post_request_inner_instance.to_dict()
# create an instance of ContentV2CardsUploadPostRequestInner from a dict
content_v2_cards_upload_post_request_inner_from_dict = ContentV2CardsUploadPostRequestInner.from_dict(content_v2_cards_upload_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



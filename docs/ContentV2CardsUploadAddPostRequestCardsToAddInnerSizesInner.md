# ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tech_size** | **str** | Размер товара (XL, 42 и др.) | [optional] 
**wb_size** | **str** | Российский размер товара | [optional] 
**price** | **int** | Цена товара | [optional] 
**skus** | **List[str]** | Баркод | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner import ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner from a JSON string
content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner_instance = ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner.to_json())

# convert the object into a dict
content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner_dict = content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner_instance.to_dict()
# create an instance of ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner from a dict
content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner_from_dict = ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner.from_dict(content_v2_cards_upload_add_post_request_cards_to_add_inner_sizes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



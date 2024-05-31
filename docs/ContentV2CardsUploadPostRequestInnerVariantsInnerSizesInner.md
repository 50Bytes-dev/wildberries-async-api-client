# ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tech_size** | **str** | Размер товара (XL, 45 и др.) | [optional] 
**wb_size** | **str** | Российский размер товара | [optional] 
**price** | **int** | Цена товара | [optional] 
**skus** | **List[str]** | Баркод. Если не указать, сгенерируется системой автоматически. | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner import ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner from a JSON string
content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner_instance = ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner.to_json())

# convert the object into a dict
content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner_dict = content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner_instance.to_dict()
# create an instance of ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner from a dict
content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner_from_dict = ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner.from_dict(content_v2_cards_upload_post_request_inner_variants_inner_sizes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



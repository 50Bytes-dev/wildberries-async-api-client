# ContentV2CardsUpdatePostRequestInnerSizesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chrt_id** | **int** | Числовой идентификатор размера для данного артикула Wildberries Обязателен к заполнению для существующих размеров. Для добавляемых размеров не указывается.  | [optional] 
**tech_size** | **str** | Размер товара (XL, S, 45 и др.) | [optional] 
**wb_size** | **str** | Российский размер товара | [optional] 
**skus** | **List[str]** | Баркод | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_update_post_request_inner_sizes_inner import ContentV2CardsUpdatePostRequestInnerSizesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUpdatePostRequestInnerSizesInner from a JSON string
content_v2_cards_update_post_request_inner_sizes_inner_instance = ContentV2CardsUpdatePostRequestInnerSizesInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUpdatePostRequestInnerSizesInner.to_json())

# convert the object into a dict
content_v2_cards_update_post_request_inner_sizes_inner_dict = content_v2_cards_update_post_request_inner_sizes_inner_instance.to_dict()
# create an instance of ContentV2CardsUpdatePostRequestInnerSizesInner from a dict
content_v2_cards_update_post_request_inner_sizes_inner_from_dict = ContentV2CardsUpdatePostRequestInnerSizesInner.from_dict(content_v2_cards_update_post_request_inner_sizes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



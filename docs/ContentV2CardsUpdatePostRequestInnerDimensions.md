# ContentV2CardsUpdatePostRequestInnerDimensions

Габариты упаковки товара. Указывать в **сантиметрах** для любого товара. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Длина, см | [optional] 
**width** | **int** | Ширина, см | [optional] 
**height** | **int** | Высота, см | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_update_post_request_inner_dimensions import ContentV2CardsUpdatePostRequestInnerDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUpdatePostRequestInnerDimensions from a JSON string
content_v2_cards_update_post_request_inner_dimensions_instance = ContentV2CardsUpdatePostRequestInnerDimensions.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUpdatePostRequestInnerDimensions.to_json())

# convert the object into a dict
content_v2_cards_update_post_request_inner_dimensions_dict = content_v2_cards_update_post_request_inner_dimensions_instance.to_dict()
# create an instance of ContentV2CardsUpdatePostRequestInnerDimensions from a dict
content_v2_cards_update_post_request_inner_dimensions_from_dict = ContentV2CardsUpdatePostRequestInnerDimensions.from_dict(content_v2_cards_update_post_request_inner_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



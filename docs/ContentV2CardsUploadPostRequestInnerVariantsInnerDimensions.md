# ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions

Габариты упаковки товара. Указывать в **сантиметрах** для любого товара.  <br>  Если не указать структуру dimensions в запросе, то она сгенерируется системой автоматически с нулевыми значениями длины, ширины, высоты 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** | Длина, см | [optional] 
**width** | **int** | Ширина, см | [optional] 
**height** | **int** | Высота, см | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_post_request_inner_variants_inner_dimensions import ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions from a JSON string
content_v2_cards_upload_post_request_inner_variants_inner_dimensions_instance = ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions.to_json())

# convert the object into a dict
content_v2_cards_upload_post_request_inner_variants_inner_dimensions_dict = content_v2_cards_upload_post_request_inner_variants_inner_dimensions_instance.to_dict()
# create an instance of ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions from a dict
content_v2_cards_upload_post_request_inner_variants_inner_dimensions_from_dict = ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions.from_dict(content_v2_cards_upload_post_request_inner_variants_inner_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



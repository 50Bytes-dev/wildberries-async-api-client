# ContentV2CardsUploadPostRequestInnerVariantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | Бренд | [optional] 
**title** | **str** | Наименование товара | [optional] 
**description** | **str** | Описание товара. Максимальное количество символов зависит от категории товара. Стандарт — 2000, минимум — 1000, максимум — 5000.&lt;br&gt; Подробно о правилах описания в **Правилах заполнения карточки товара** в разделе [Инструкции](https://seller.wildberries.ru/training) на портале продавцов.  | [optional] 
**vendor_code** | **str** | Артикул продавца | 
**dimensions** | [**ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions**](ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions.md) |  | [optional] 
**sizes** | [**List[ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner]**](ContentV2CardsUploadPostRequestInnerVariantsInnerSizesInner.md) | Массив с размерами. &lt;br&gt;  Если для размерного товара (обувь, одежда и др.) не указать этот массив, то системой в карточке он будет сгенерирован автоматически с &#x60;techSize&#x60; &#x3D; \&quot;A\&quot; и &#x60;wbSize&#x60; &#x3D; \&quot;1\&quot; и баркодом.  | [optional] 
**characteristics** | [**List[ContentV2CardsUploadPostRequestInnerVariantsInnerCharacteristicsInner]**](ContentV2CardsUploadPostRequestInnerVariantsInnerCharacteristicsInner.md) | Массив характеристик товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_post_request_inner_variants_inner import ContentV2CardsUploadPostRequestInnerVariantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadPostRequestInnerVariantsInner from a JSON string
content_v2_cards_upload_post_request_inner_variants_inner_instance = ContentV2CardsUploadPostRequestInnerVariantsInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadPostRequestInnerVariantsInner.to_json())

# convert the object into a dict
content_v2_cards_upload_post_request_inner_variants_inner_dict = content_v2_cards_upload_post_request_inner_variants_inner_instance.to_dict()
# create an instance of ContentV2CardsUploadPostRequestInnerVariantsInner from a dict
content_v2_cards_upload_post_request_inner_variants_inner_from_dict = ContentV2CardsUploadPostRequestInnerVariantsInner.from_dict(content_v2_cards_upload_post_request_inner_variants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



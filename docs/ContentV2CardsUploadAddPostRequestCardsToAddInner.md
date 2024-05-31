# ContentV2CardsUploadAddPostRequestCardsToAddInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | Бренд | [optional] 
**vendor_code** | **str** | Артикул продавца | 
**title** | **str** | Наименование товара | [optional] 
**description** | **str** | Описание товара. Максимальное количество символов зависит от категории товара. Стандарт — 2000, минимум — 1000, максимум — 5000.&lt;br&gt; Подробно о правилах описания в **Правилах заполнения карточки товара** в разделе [Инструкции](https://seller.wildberries.ru/training) на портале продавцов.  | [optional] 
**dimensions** | [**ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions**](ContentV2CardsUploadPostRequestInnerVariantsInnerDimensions.md) |  | [optional] 
**characteristics** | [**List[ContentV2CardsUploadAddPostRequestCardsToAddInnerCharacteristicsInner]**](ContentV2CardsUploadAddPostRequestCardsToAddInnerCharacteristicsInner.md) | Характеристики товара | [optional] 
**sizes** | [**List[ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner]**](ContentV2CardsUploadAddPostRequestCardsToAddInnerSizesInner.md) | Массив с размерами. &lt;br&gt;  Если для размерного товара (обувь, одежда и др.) не указать этот массив, то системой в карточке он будет сгенерирован автоматически с &#x60;techSize&#x60; &#x3D; \&quot;A\&quot; и &#x60;wbSize&#x60; &#x3D; \&quot;1\&quot; и баркодом.  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_upload_add_post_request_cards_to_add_inner import ContentV2CardsUploadAddPostRequestCardsToAddInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUploadAddPostRequestCardsToAddInner from a JSON string
content_v2_cards_upload_add_post_request_cards_to_add_inner_instance = ContentV2CardsUploadAddPostRequestCardsToAddInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUploadAddPostRequestCardsToAddInner.to_json())

# convert the object into a dict
content_v2_cards_upload_add_post_request_cards_to_add_inner_dict = content_v2_cards_upload_add_post_request_cards_to_add_inner_instance.to_dict()
# create an instance of ContentV2CardsUploadAddPostRequestCardsToAddInner from a dict
content_v2_cards_upload_add_post_request_cards_to_add_inner_from_dict = ContentV2CardsUploadAddPostRequestCardsToAddInner.from_dict(content_v2_cards_upload_add_post_request_cards_to_add_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


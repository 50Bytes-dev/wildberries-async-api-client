# ContentV2CardsUpdatePostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | 
**vendor_code** | **str** | Артикул продавца | 
**brand** | **str** | Бренд | [optional] 
**title** | **str** | Наименование товара | [optional] 
**description** | **str** | Описание товара. Максимальное количество символов зависит от категории товара. Стандарт — 2000, минимум — 1000, максимум — 5000.&lt;br&gt; Подробно о правилах описания в **Правилах заполнения карточки товара** в разделе [Инструкции](https://seller.wildberries.ru/training) на портале продавцов.  | [optional] 
**dimensions** | [**ContentV2CardsUpdatePostRequestInnerDimensions**](ContentV2CardsUpdatePostRequestInnerDimensions.md) |  | [optional] 
**characteristics** | [**List[ContentV2CardsUpdatePostRequestInnerCharacteristicsInner]**](ContentV2CardsUpdatePostRequestInnerCharacteristicsInner.md) | Характеристики товара | [optional] 
**sizes** | [**List[ContentV2CardsUpdatePostRequestInnerSizesInner]**](ContentV2CardsUpdatePostRequestInnerSizesInner.md) | Массив размеров артикула. &lt;br&gt; Для безразмерного товара все равно нужно передавать данный массив без параметров (wbSize и techSize), но с баркодом.                            | 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_update_post_request_inner import ContentV2CardsUpdatePostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsUpdatePostRequestInner from a JSON string
content_v2_cards_update_post_request_inner_instance = ContentV2CardsUpdatePostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsUpdatePostRequestInner.to_json())

# convert the object into a dict
content_v2_cards_update_post_request_inner_dict = content_v2_cards_update_post_request_inner_instance.to_dict()
# create an instance of ContentV2CardsUpdatePostRequestInner from a dict
content_v2_cards_update_post_request_inner_from_dict = ContentV2CardsUpdatePostRequestInner.from_dict(content_v2_cards_update_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



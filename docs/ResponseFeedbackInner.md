# ResponseFeedbackInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id отзыва | [optional] 
**user_name** | **str** | Имя автора отзыва | [optional] 
**matching_size** | **str** | Соответствие заявленного размера реальному. &lt;br&gt;Возможные значения: - &#x60; &#x60; - для безразмерных товаров - &#x60;ок&#x60; - соответствует размеру - &#x60;smaller&#x60; - маломерит - &#x60;bigger&#x60; - большемерит          | [optional] 
**text** | **str** | Текст отзыва | [optional] 
**product_valuation** | **int** | Оценка товара от покупателя | [optional] 
**created_date** | **datetime** | Дата и время создания отзыва | [optional] 
**state** | **str** | Статус отзыва:   - &#x60;none&#x60; - не обработан (новый)   - &#x60;wbRu&#x60; - обработан  | [optional] 
**answer** | [**ResponseFeedbackInnerAnswer**](ResponseFeedbackInnerAnswer.md) |  | [optional] 
**product_details** | [**ApiV1FeedbackGet200ResponseDataProductDetails**](ApiV1FeedbackGet200ResponseDataProductDetails.md) |  | [optional] 
**photo_links** | [**List[ApiV1FeedbackGet200ResponseDataPhotoLinksInner]**](ApiV1FeedbackGet200ResponseDataPhotoLinksInner.md) | Массив структур фотографий | [optional] 
**video** | [**ApiV1FeedbackGet200ResponseDataVideo**](ApiV1FeedbackGet200ResponseDataVideo.md) |  | [optional] 
**was_viewed** | **bool** | Просмотрен ли отзыв | [optional] 
**is_able_supplier_feedback_valuation** | **bool** | Доступна ли продавцу оценка отзыва (&#x60;true&#x60; - доступна, &#x60;false&#x60; - не доступна) | [optional] 
**supplier_feedback_valuation** | **int** | Оценка отзыва, оставленная продавцом | [optional] 
**is_able_supplier_product_valuation** | **bool** | Доступна ли продавцу оценка товара (&#x60;true&#x60; - доступна, &#x60;false&#x60; - не доступна) | [optional] 
**supplier_product_valuation** | **int** | Оценка товара, оставленная продавцом | [optional] 
**is_able_return_product_orders** | **bool** | Доступна ли товару опция возврата (&#x60;false&#x60; - нет, &#x60;true&#x60; - да) | [optional] 
**return_product_orders_date** | **str** | Дата и время, когда на запрос возврата был получен ответ со статус-кодом 200. | [optional] 
**bables** | **List[str]** | Список тегов покупателя | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_feedback_inner import ResponseFeedbackInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseFeedbackInner from a JSON string
response_feedback_inner_instance = ResponseFeedbackInner.from_json(json)
# print the JSON string representation of the object
print(ResponseFeedbackInner.to_json())

# convert the object into a dict
response_feedback_inner_dict = response_feedback_inner_instance.to_dict()
# create an instance of ResponseFeedbackInner from a dict
response_feedback_inner_from_dict = ResponseFeedbackInner.from_dict(response_feedback_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



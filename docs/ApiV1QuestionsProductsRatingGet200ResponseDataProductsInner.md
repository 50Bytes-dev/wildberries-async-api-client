# ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**imt_id** | **int** | Идентификатор карточки товара | [optional] 
**product_name** | **str** | Название товара | [optional] 
**brand_name** | **str** | Бренд товара | [optional] 
**questions_count** | **str** | Количество вопросов | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_products_rating_get200_response_data_products_inner import ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner from a JSON string
api_v1_questions_products_rating_get200_response_data_products_inner_instance = ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner.to_json())

# convert the object into a dict
api_v1_questions_products_rating_get200_response_data_products_inner_dict = api_v1_questions_products_rating_get200_response_data_products_inner_instance.to_dict()
# create an instance of ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner from a dict
api_v1_questions_products_rating_get200_response_data_products_inner_from_dict = ApiV1QuestionsProductsRatingGet200ResponseDataProductsInner.from_dict(api_v1_questions_products_rating_get200_response_data_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



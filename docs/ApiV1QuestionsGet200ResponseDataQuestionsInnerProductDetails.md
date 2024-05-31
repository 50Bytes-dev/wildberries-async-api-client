# ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails

Структура товара

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**imt_id** | **int** | Идентификатор карточки товара | [optional] 
**product_name** | **str** | Название товара | [optional] 
**supplier_article** | **str** | Артикул продавца | [optional] 
**supplier_name** | **str** | Имя продавца | [optional] 
**brand_name** | **str** | Название бренда | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_questions_get200_response_data_questions_inner_product_details import ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails from a JSON string
api_v1_questions_get200_response_data_questions_inner_product_details_instance = ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails.from_json(json)
# print the JSON string representation of the object
print(ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails.to_json())

# convert the object into a dict
api_v1_questions_get200_response_data_questions_inner_product_details_dict = api_v1_questions_get200_response_data_questions_inner_product_details_instance.to_dict()
# create an instance of ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails from a dict
api_v1_questions_get200_response_data_questions_inner_product_details_from_dict = ApiV1QuestionsGet200ResponseDataQuestionsInnerProductDetails.from_dict(api_v1_questions_get200_response_data_questions_inner_product_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ProductRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**imt_id** | **int** | Идентификатор карточки товара | [optional] 
**valuations_sum** | **int** | Сумма оценок | [optional] 
**feedbacks_count** | **int** | Количество отзывов | [optional] 
**valuation** | **float** | Средняя оценка | [optional] 
**product_name** | **str** | Название товара | [optional] 
**supplier_article** | **str** | Артикул продавца | [optional] 
**brand_name** | **str** | Бренд товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.product_rating import ProductRating

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRating from a JSON string
product_rating_instance = ProductRating.from_json(json)
# print the JSON string representation of the object
print(ProductRating.to_json())

# convert the object into a dict
product_rating_dict = product_rating_instance.to_dict()
# create an instance of ProductRating from a dict
product_rating_from_dict = ProductRating.from_dict(product_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



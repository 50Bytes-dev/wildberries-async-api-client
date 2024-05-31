# ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_max_rating** | [**ProductRating**](ProductRating.md) |  | [optional] 
**product_min_rating** | [**ProductRating**](ProductRating.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_products_rating_top_get200_response_data_inner import ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner from a JSON string
api_v1_feedbacks_products_rating_top_get200_response_data_inner_instance = ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_feedbacks_products_rating_top_get200_response_data_inner_dict = api_v1_feedbacks_products_rating_top_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner from a dict
api_v1_feedbacks_products_rating_top_get200_response_data_inner_from_dict = ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner.from_dict(api_v1_feedbacks_products_rating_top_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



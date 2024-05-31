# ApiV1FeedbacksProductsRatingTopGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner]**](ApiV1FeedbacksProductsRatingTopGet200ResponseDataInner.md) |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_products_rating_top_get200_response import ApiV1FeedbacksProductsRatingTopGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksProductsRatingTopGet200Response from a JSON string
api_v1_feedbacks_products_rating_top_get200_response_instance = ApiV1FeedbacksProductsRatingTopGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksProductsRatingTopGet200Response.to_json())

# convert the object into a dict
api_v1_feedbacks_products_rating_top_get200_response_dict = api_v1_feedbacks_products_rating_top_get200_response_instance.to_dict()
# create an instance of ApiV1FeedbacksProductsRatingTopGet200Response from a dict
api_v1_feedbacks_products_rating_top_get200_response_from_dict = ApiV1FeedbacksProductsRatingTopGet200Response.from_dict(api_v1_feedbacks_products_rating_top_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



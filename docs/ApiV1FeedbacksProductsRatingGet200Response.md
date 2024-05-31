# ApiV1FeedbacksProductsRatingGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiV1FeedbacksProductsRatingGet200ResponseData**](ApiV1FeedbacksProductsRatingGet200ResponseData.md) |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_products_rating_get200_response import ApiV1FeedbacksProductsRatingGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksProductsRatingGet200Response from a JSON string
api_v1_feedbacks_products_rating_get200_response_instance = ApiV1FeedbacksProductsRatingGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksProductsRatingGet200Response.to_json())

# convert the object into a dict
api_v1_feedbacks_products_rating_get200_response_dict = api_v1_feedbacks_products_rating_get200_response_instance.to_dict()
# create an instance of ApiV1FeedbacksProductsRatingGet200Response from a dict
api_v1_feedbacks_products_rating_get200_response_from_dict = ApiV1FeedbacksProductsRatingGet200Response.from_dict(api_v1_feedbacks_products_rating_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


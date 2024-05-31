# ContentV2CardsLimitsGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_limits** | **int** | Количество бесплатных лимитов | [optional] 
**paid_limits** | **int** | Количество оплаченных лимитов | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_limits_get200_response_data import ContentV2CardsLimitsGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsLimitsGet200ResponseData from a JSON string
content_v2_cards_limits_get200_response_data_instance = ContentV2CardsLimitsGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsLimitsGet200ResponseData.to_json())

# convert the object into a dict
content_v2_cards_limits_get200_response_data_dict = content_v2_cards_limits_get200_response_data_instance.to_dict()
# create an instance of ContentV2CardsLimitsGet200ResponseData from a dict
content_v2_cards_limits_get200_response_data_from_dict = ContentV2CardsLimitsGet200ResponseData.from_dict(content_v2_cards_limits_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



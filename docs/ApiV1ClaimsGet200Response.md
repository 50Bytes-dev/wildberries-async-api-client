# ApiV1ClaimsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**List[ApiV1ClaimsGet200ResponseClaimsInner]**](ApiV1ClaimsGet200ResponseClaimsInner.md) | Заявки | [optional] 
**total** | **int** | Количество заявок, соответствующих параметрам запроса. Без учёта &#x60;limit&#x60; и &#x60;offset&#x60; | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_claims_get200_response import ApiV1ClaimsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ClaimsGet200Response from a JSON string
api_v1_claims_get200_response_instance = ApiV1ClaimsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1ClaimsGet200Response.to_json())

# convert the object into a dict
api_v1_claims_get200_response_dict = api_v1_claims_get200_response_instance.to_dict()
# create an instance of ApiV1ClaimsGet200Response from a dict
api_v1_claims_get200_response_from_dict = ApiV1ClaimsGet200Response.from_dict(api_v1_claims_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



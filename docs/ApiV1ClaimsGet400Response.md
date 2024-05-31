# ApiV1ClaimsGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | ID ошибки | [optional] 
**detail** | **str** | Описание ошибки | [optional] 
**request_id** | **str** | ID запроса | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_claims_get400_response import ApiV1ClaimsGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ClaimsGet400Response from a JSON string
api_v1_claims_get400_response_instance = ApiV1ClaimsGet400Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1ClaimsGet400Response.to_json())

# convert the object into a dict
api_v1_claims_get400_response_dict = api_v1_claims_get400_response_instance.to_dict()
# create an instance of ApiV1ClaimsGet400Response from a dict
api_v1_claims_get400_response_from_dict = ApiV1ClaimsGet400Response.from_dict(api_v1_claims_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



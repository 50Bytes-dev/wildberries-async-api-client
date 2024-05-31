# ApiV1ClaimsGet429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Код ошибки | [optional] 
**message** | **str** | Описание ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_claims_get429_response import ApiV1ClaimsGet429Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ClaimsGet429Response from a JSON string
api_v1_claims_get429_response_instance = ApiV1ClaimsGet429Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1ClaimsGet429Response.to_json())

# convert the object into a dict
api_v1_claims_get429_response_dict = api_v1_claims_get429_response_instance.to_dict()
# create an instance of ApiV1ClaimsGet429Response from a dict
api_v1_claims_get429_response_from_dict = ApiV1ClaimsGet429Response.from_dict(api_v1_claims_get429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



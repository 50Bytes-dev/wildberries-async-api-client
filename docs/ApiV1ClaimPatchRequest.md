# ApiV1ClaimPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID заявки | [optional] 
**action** | **str** | Действие с заявкой.&lt;br&gt;Используйте одно из значений массива &#x60;actions&#x60; — ответа [метода получения заявок](./#/paths/~1api~1v1~1claims/get) | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_claim_patch_request import ApiV1ClaimPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ClaimPatchRequest from a JSON string
api_v1_claim_patch_request_instance = ApiV1ClaimPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV1ClaimPatchRequest.to_json())

# convert the object into a dict
api_v1_claim_patch_request_dict = api_v1_claim_patch_request_instance.to_dict()
# create an instance of ApiV1ClaimPatchRequest from a dict
api_v1_claim_patch_request_from_dict = ApiV1ClaimPatchRequest.from_dict(api_v1_claim_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



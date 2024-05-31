# ApiV1ListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiV1ListPost200ResponseDataInner]**](ApiV1ListPost200ResponseDataInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_list_post200_response import ApiV1ListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ListPost200Response from a JSON string
api_v1_list_post200_response_instance = ApiV1ListPost200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV1ListPost200Response.to_json())

# convert the object into a dict
api_v1_list_post200_response_dict = api_v1_list_post200_response_instance.to_dict()
# create an instance of ApiV1ListPost200Response from a dict
api_v1_list_post200_response_from_dict = ApiV1ListPost200Response.from_dict(api_v1_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# ApiV3SuppliesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Наименование поставки | [optional] 

## Example

```python
from wb_client.models.api_v3_supplies_post_request import ApiV3SuppliesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3SuppliesPostRequest from a JSON string
api_v3_supplies_post_request_instance = ApiV3SuppliesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3SuppliesPostRequest.to_json())

# convert the object into a dict
api_v3_supplies_post_request_dict = api_v3_supplies_post_request_instance.to_dict()
# create an instance of ApiV3SuppliesPostRequest from a dict
api_v3_supplies_post_request_from_dict = ApiV3SuppliesPostRequest.from_dict(api_v3_supplies_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV1SearchSetPlusPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pluse** | **List[str]** | Список фиксированных фраз (max. 100) | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_search_set_plus_post_request import AdvV1SearchSetPlusPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1SearchSetPlusPostRequest from a JSON string
adv_v1_search_set_plus_post_request_instance = AdvV1SearchSetPlusPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1SearchSetPlusPostRequest.to_json())

# convert the object into a dict
adv_v1_search_set_plus_post_request_dict = adv_v1_search_set_plus_post_request_instance.to_dict()
# create an instance of AdvV1SearchSetPlusPostRequest from a dict
adv_v1_search_set_plus_post_request_from_dict = AdvV1SearchSetPlusPostRequest.from_dict(adv_v1_search_set_plus_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV1AutoSetExcludedPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excluded** | **List[str]** | Список фраз (макс. 1000 шт.) | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_auto_set_excluded_post_request import AdvV1AutoSetExcludedPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AutoSetExcludedPostRequest from a JSON string
adv_v1_auto_set_excluded_post_request_instance = AdvV1AutoSetExcludedPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1AutoSetExcludedPostRequest.to_json())

# convert the object into a dict
adv_v1_auto_set_excluded_post_request_dict = adv_v1_auto_set_excluded_post_request_instance.to_dict()
# create an instance of AdvV1AutoSetExcludedPostRequest from a dict
adv_v1_auto_set_excluded_post_request_from_dict = AdvV1AutoSetExcludedPostRequest.from_dict(adv_v1_auto_set_excluded_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



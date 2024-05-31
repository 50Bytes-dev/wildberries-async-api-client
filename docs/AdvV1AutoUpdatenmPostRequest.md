# AdvV1AutoUpdatenmPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[int]** | Номенклатуры, которые необходимо добавить. | [optional] 
**delete** | **List[int]** | Номенклатуры, которые необходимо удалить. | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_auto_updatenm_post_request import AdvV1AutoUpdatenmPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AutoUpdatenmPostRequest from a JSON string
adv_v1_auto_updatenm_post_request_instance = AdvV1AutoUpdatenmPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1AutoUpdatenmPostRequest.to_json())

# convert the object into a dict
adv_v1_auto_updatenm_post_request_dict = adv_v1_auto_updatenm_post_request_instance.to_dict()
# create an instance of AdvV1AutoUpdatenmPostRequest from a dict
adv_v1_auto_updatenm_post_request_from_dict = AdvV1AutoUpdatenmPostRequest.from_dict(adv_v1_auto_updatenm_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



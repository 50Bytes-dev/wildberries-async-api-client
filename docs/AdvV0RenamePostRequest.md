# AdvV0RenamePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | Идентификатор кампании, у которой меняется название | 
**name** | **str** | Новое название (максимум 100 символов) | 

## Example

```python
from wildberries_async_api_client.models.adv_v0_rename_post_request import AdvV0RenamePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV0RenamePostRequest from a JSON string
adv_v0_rename_post_request_instance = AdvV0RenamePostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV0RenamePostRequest.to_json())

# convert the object into a dict
adv_v0_rename_post_request_dict = adv_v0_rename_post_request_instance.to_dict()
# create an instance of AdvV0RenamePostRequest from a dict
adv_v0_rename_post_request_from_dict = AdvV0RenamePostRequest.from_dict(adv_v0_rename_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



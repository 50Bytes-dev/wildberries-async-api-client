# PatchDelRespOK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bool** |  | [optional] 
**error** | **bool** | Есть ли ошибка | [optional] 
**error_text** | **str** | Описание ошибки | [optional] 
**additional_errors** | **List[str]** | Дополнительные ошибки | [optional] 

## Example

```python
from wildberries_async_api_client.models.patch_del_resp_ok import PatchDelRespOK

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDelRespOK from a JSON string
patch_del_resp_ok_instance = PatchDelRespOK.from_json(json)
# print the JSON string representation of the object
print(PatchDelRespOK.to_json())

# convert the object into a dict
patch_del_resp_ok_dict = patch_del_resp_ok_instance.to_dict()
# create an instance of PatchDelRespOK from a dict
patch_del_resp_ok_from_dict = PatchDelRespOK.from_dict(patch_del_resp_ok_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



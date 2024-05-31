# AdvV0ParamsSubjectGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Значение для параметра &#x60;subjectId&#x60; | [optional] 
**name** | **str** | Название предметной группы, для которой создана кампания | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v0_params_subject_get200_response_inner import AdvV0ParamsSubjectGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV0ParamsSubjectGet200ResponseInner from a JSON string
adv_v0_params_subject_get200_response_inner_instance = AdvV0ParamsSubjectGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(AdvV0ParamsSubjectGet200ResponseInner.to_json())

# convert the object into a dict
adv_v0_params_subject_get200_response_inner_dict = adv_v0_params_subject_get200_response_inner_instance.to_dict()
# create an instance of AdvV0ParamsSubjectGet200ResponseInner from a dict
adv_v0_params_subject_get200_response_inner_from_dict = AdvV0ParamsSubjectGet200ResponseInner.from_dict(adv_v0_params_subject_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



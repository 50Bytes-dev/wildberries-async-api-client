# ApiV1ParentSubjectsGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_id** | **int** | Id категории товара | [optional] 
**subject_name** | **str** | Название категории товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_parent_subjects_get200_response_data_inner import ApiV1ParentSubjectsGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ParentSubjectsGet200ResponseDataInner from a JSON string
api_v1_parent_subjects_get200_response_data_inner_instance = ApiV1ParentSubjectsGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1ParentSubjectsGet200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_parent_subjects_get200_response_data_inner_dict = api_v1_parent_subjects_get200_response_data_inner_instance.to_dict()
# create an instance of ApiV1ParentSubjectsGet200ResponseDataInner from a dict
api_v1_parent_subjects_get200_response_data_inner_from_dict = ApiV1ParentSubjectsGet200ResponseDataInner.from_dict(api_v1_parent_subjects_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



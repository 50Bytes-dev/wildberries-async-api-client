# ApiV1ListPost200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm** | **int** | Артикул WB, по которому запрошены рекомендации. | [optional] 
**list** | **List[int]** | Список рекомендаций | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_list_post200_response_data_inner import ApiV1ListPost200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1ListPost200ResponseDataInner from a JSON string
api_v1_list_post200_response_data_inner_instance = ApiV1ListPost200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1ListPost200ResponseDataInner.to_json())

# convert the object into a dict
api_v1_list_post200_response_data_inner_dict = api_v1_list_post200_response_data_inner_instance.to_dict()
# create an instance of ApiV1ListPost200ResponseDataInner from a dict
api_v1_list_post200_response_data_inner_from_dict = ApiV1ListPost200ResponseDataInner.from_dict(api_v1_list_post200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



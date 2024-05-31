# ResponseInfoAdvertType9UnitedParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**ResponseInfoAdvertType9UnitedParamsInnerSubject**](ResponseInfoAdvertType9UnitedParamsInnerSubject.md) |  | [optional] 
**menus** | [**List[ResponseInfoAdvertType9UnitedParamsInnerMenusInner]**](ResponseInfoAdvertType9UnitedParamsInnerMenusInner.md) |  | [optional] 
**nms** | **List[int]** | Артикулы WB | [optional] 
**search_cpm** | **int** | Ставка в Поиске. | [optional] 
**catalog_cpm** | **int** | Ставка в Каталоге, при наличии. | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert_type9_united_params_inner import ResponseInfoAdvertType9UnitedParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvertType9UnitedParamsInner from a JSON string
response_info_advert_type9_united_params_inner_instance = ResponseInfoAdvertType9UnitedParamsInner.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvertType9UnitedParamsInner.to_json())

# convert the object into a dict
response_info_advert_type9_united_params_inner_dict = response_info_advert_type9_united_params_inner_instance.to_dict()
# create an instance of ResponseInfoAdvertType9UnitedParamsInner from a dict
response_info_advert_type9_united_params_inner_from_dict = ResponseInfoAdvertType9UnitedParamsInner.from_dict(response_info_advert_type9_united_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



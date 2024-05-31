# ResponseInfoAdvertType8AutoParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**ResponseInfoAdvertType8AutoParamsSubject**](ResponseInfoAdvertType8AutoParamsSubject.md) |  | [optional] 
**sets** | [**List[ResponseInfoAdvertType8AutoParamsSetsInner]**](ResponseInfoAdvertType8AutoParamsSetsInner.md) | Внутренняя (системная) сущность (пол + предмет) | [optional] 
**menus** | [**List[ResponseInfoAdvertType8AutoParamsMenusInner]**](ResponseInfoAdvertType8AutoParamsMenusInner.md) |  | [optional] 
**active** | [**ResponseInfoAdvertType8AutoParamsActive**](ResponseInfoAdvertType8AutoParamsActive.md) |  | [optional] 
**nm_cpm** | [**List[ResponseInfoAdvertType8AutoParamsNmCPMInner]**](ResponseInfoAdvertType8AutoParamsNmCPMInner.md) | Ставки номенклатур (артикулов WB)  | [optional] 
**nms** | **List[int]** | Артикулы WB | [optional] 
**cpm** | **int** | Ставка, указанная при создании кампании.&lt;br&gt;  Поле актуально только для кампаний, созданных через API.    | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert_type8_auto_params import ResponseInfoAdvertType8AutoParams

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvertType8AutoParams from a JSON string
response_info_advert_type8_auto_params_instance = ResponseInfoAdvertType8AutoParams.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvertType8AutoParams.to_json())

# convert the object into a dict
response_info_advert_type8_auto_params_dict = response_info_advert_type8_auto_params_instance.to_dict()
# create an instance of ResponseInfoAdvertType8AutoParams from a dict
response_info_advert_type8_auto_params_from_dict = ResponseInfoAdvertType8AutoParams.from_dict(response_info_advert_type8_auto_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



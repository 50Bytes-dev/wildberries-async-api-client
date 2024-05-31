# ResponseInfoAdvertType8AutoParamsActive

Зоны показов

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carousel** | **bool** | Карточка товара (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены) | [optional] 
**recom** | **bool** | Рекомендации на главной (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены) | [optional] 
**booster** | **bool** | Поиск/Каталог (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены) | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert_type8_auto_params_active import ResponseInfoAdvertType8AutoParamsActive

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvertType8AutoParamsActive from a JSON string
response_info_advert_type8_auto_params_active_instance = ResponseInfoAdvertType8AutoParamsActive.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvertType8AutoParamsActive.to_json())

# convert the object into a dict
response_info_advert_type8_auto_params_active_dict = response_info_advert_type8_auto_params_active_instance.to_dict()
# create an instance of ResponseInfoAdvertType8AutoParamsActive from a dict
response_info_advert_type8_auto_params_active_from_dict = ResponseInfoAdvertType8AutoParamsActive.from_dict(response_info_advert_type8_auto_params_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ResponseInfoAdvertParamsInnerNmsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm** | **int** | Числовой идентификатор номенклатуры Wildberries (&lt;code&gt;nmId&lt;/code&gt;) | [optional] 
**active** | **bool** | Состояние номенклатуры (&lt;code&gt;true&lt;/code&gt; - активна или &lt;code&gt;false&lt;/code&gt; - неактивна) | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_info_advert_params_inner_nms_inner import ResponseInfoAdvertParamsInnerNmsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseInfoAdvertParamsInnerNmsInner from a JSON string
response_info_advert_params_inner_nms_inner_instance = ResponseInfoAdvertParamsInnerNmsInner.from_json(json)
# print the JSON string representation of the object
print(ResponseInfoAdvertParamsInnerNmsInner.to_json())

# convert the object into a dict
response_info_advert_params_inner_nms_inner_dict = response_info_advert_params_inner_nms_inner_instance.to_dict()
# create an instance of ResponseInfoAdvertParamsInnerNmsInner from a dict
response_info_advert_params_inner_nms_inner_from_dict = ResponseInfoAdvertParamsInnerNmsInner.from_dict(response_info_advert_params_inner_nms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelsOptionsResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[ModelsOptionsResultModelResultInner]**](ModelsOptionsResultModelResultInner.md) |  | [optional] 
**request_id** | **str** | ID запроса при наличии ошибок | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_options_result_model import ModelsOptionsResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsOptionsResultModel from a JSON string
models_options_result_model_instance = ModelsOptionsResultModel.from_json(json)
# print the JSON string representation of the object
print(ModelsOptionsResultModel.to_json())

# convert the object into a dict
models_options_result_model_dict = models_options_result_model_instance.to_dict()
# create an instance of ModelsOptionsResultModel from a dict
models_options_result_model_from_dict = ModelsOptionsResultModel.from_dict(models_options_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



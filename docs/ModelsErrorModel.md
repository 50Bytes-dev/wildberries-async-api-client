# ModelsErrorModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP статус-код | [optional] 
**title** | **str** | ID ошибки | [optional] 
**detail** | **str** | Описание ошибки | [optional] 
**request_id** | **str** | ID запроса | [optional] 
**origin** | **str** | Сервис, вернувший ошибку | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_error_model import ModelsErrorModel

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsErrorModel from a JSON string
models_error_model_instance = ModelsErrorModel.from_json(json)
# print the JSON string representation of the object
print(ModelsErrorModel.to_json())

# convert the object into a dict
models_error_model_dict = models_error_model_instance.to_dict()
# create an instance of ModelsErrorModel from a dict
models_error_model_from_dict = ModelsErrorModel.from_dict(models_error_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



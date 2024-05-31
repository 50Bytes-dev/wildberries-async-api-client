# ModelPass

Данные о пропуске продавца

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Имя водителя | [optional] 
**date_end** | **str** | Дата окончания действия пропуска | [optional] 
**last_name** | **str** | Фамилия водителя | [optional] 
**car_model** | **str** | Марка машины | [optional] 
**car_number** | **str** | Номер машины | [optional] 
**office_name** | **str** | Название склада | [optional] 
**office_address** | **str** | Адрес склада | [optional] 
**office_id** | **int** | ID склада | [optional] 
**id** | **int** | ID пропуска | [optional] 

## Example

```python
from wb_client.models.model_pass import ModelPass

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPass from a JSON string
model_pass_instance = ModelPass.from_json(json)
# print the JSON string representation of the object
print(ModelPass.to_json())

# convert the object into a dict
model_pass_dict = model_pass_instance.to_dict()
# create an instance of ModelPass from a dict
model_pass_from_dict = ModelPass.from_dict(model_pass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PassOffice

Данные о складе, для которого требуется пропуск

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Название | [optional] 
**address** | **str** | Адрес | [optional] 
**id** | **int** | ID | [optional] 

## Example

```python
from wb_client.models.pass_office import PassOffice

# TODO update the JSON string below
json = "{}"
# create an instance of PassOffice from a JSON string
pass_office_instance = PassOffice.from_json(json)
# print the JSON string representation of the object
print(PassOffice.to_json())

# convert the object into a dict
pass_office_dict = pass_office_instance.to_dict()
# create an instance of PassOffice from a dict
pass_office_from_dict = PassOffice.from_dict(pass_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



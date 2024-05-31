# File


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Тип файла | [optional] 
**var_date** | **str** | Дата загрузки файла | [optional] 
**name** | **str** | Название файла | [optional] 
**url** | **str** | URL для получения файла | [optional] 
**size** | **int** | Размер файла в байтах | [optional] 

## Example

```python
from wildberries_async_api_client.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charc_id** | **int** | Идентификатор характеристики | [optional] 
**subject_name** | **str** | Название предмета | [optional] 
**subject_id** | **int** | Идентификатор предмета | [optional] 
**name** | **str** | Название характеристики | [optional] 
**required** | **bool** | true - характеристику необходимо обязательно указать в КТ. false - характеристику не обязательно указывать | [optional] 
**unit_name** | **str** | Единица измерения | [optional] 
**max_count** | **int** | Максимальное кол-во значений, которое можно присвоить данной характеристике. Если 0, то нет ограничения.  | [optional] 
**popular** | **bool** | Характеристика популярна у пользователей (true - да, false - нет) | [optional] 
**charc_type** | **int** | Тип характеристики (1 и 0 - строка или массив строк; 4 - число или массив чисел) | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_object_charcs_subject_id_get200_response_data_inner import ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner from a JSON string
content_v2_object_charcs_subject_id_get200_response_data_inner_instance = ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner.to_json())

# convert the object into a dict
content_v2_object_charcs_subject_id_get200_response_data_inner_dict = content_v2_object_charcs_subject_id_get200_response_data_inner_instance.to_dict()
# create an instance of ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner from a dict
content_v2_object_charcs_subject_id_get200_response_data_inner_from_dict = ContentV2ObjectCharcsSubjectIdGet200ResponseDataInner.from_dict(content_v2_object_charcs_subject_id_get200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



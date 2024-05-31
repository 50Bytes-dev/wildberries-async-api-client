# GroupedByObjectsBrandsAndTagsReqParams

Параметры отчёта

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_ids** | **List[int]** | Идентификаторы предметов | [optional] 
**brand_names** | **List[str]** | Бренды | [optional] 
**tag_ids** | **List[int]** | Идентификаторы тегов | [optional] 
**start_date** | **date** | Начало периода | 
**end_date** | **date** | Конец периода | 
**timezone** | **str** | Временная зона, по умолчанию Europe/Moscow  | [optional] 
**aggregation_level** | **str** | Как сгруппировать данные (по умолчанию по дням):    * &#x60;day&#x60; — по дням   * &#x60;week&#x60; — по неделям   * &#x60;month&#x60; — по месяцам  | [optional] 
**skip_deleted_nm** | **bool** | Скрыть удалённые &#x60;nmID&#x60; | [optional] 

## Example

```python
from wildberries_async_api_client.models.grouped_by_objects_brands_and_tags_req_params import GroupedByObjectsBrandsAndTagsReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedByObjectsBrandsAndTagsReqParams from a JSON string
grouped_by_objects_brands_and_tags_req_params_instance = GroupedByObjectsBrandsAndTagsReqParams.from_json(json)
# print the JSON string representation of the object
print(GroupedByObjectsBrandsAndTagsReqParams.to_json())

# convert the object into a dict
grouped_by_objects_brands_and_tags_req_params_dict = grouped_by_objects_brands_and_tags_req_params_instance.to_dict()
# create an instance of GroupedByObjectsBrandsAndTagsReqParams from a dict
grouped_by_objects_brands_and_tags_req_params_from_dict = GroupedByObjectsBrandsAndTagsReqParams.from_dict(grouped_by_objects_brands_and_tags_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



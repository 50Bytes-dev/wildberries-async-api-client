# BySelectedNmIDReqParams

Параметры отчёта

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_ids** | **List[int]** | &#x60;nmID &#x60;, по которым составить отчёт. Оставьте пустым, чтобы получить отчёт по всем товарам  | [optional] 
**subject_ids** | **List[int]** | Идентификаторы предметов | [optional] 
**brand_names** | **List[str]** | Бренды | [optional] 
**tag_ids** | **List[int]** | Идентификаторы тегов | [optional] 
**start_date** | **date** | Начало периода | 
**end_date** | **date** | Конец периода | 
**timezone** | **str** | Временная зона, по умолчанию Europe/Moscow  | [optional] 
**aggregation_level** | **str** | Как сгруппировать данные (по умолчанию по дням):    * &#x60;day&#x60; — по дням   * &#x60;week&#x60; — по неделям   * &#x60;month&#x60; — по месяцам  | [optional] 
**skip_deleted_nm** | **bool** | Скрыть удалённые номенклатуры | [optional] 

## Example

```python
from wildberries_async_api_client.models.by_selected_nm_id_req_params import BySelectedNmIDReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of BySelectedNmIDReqParams from a JSON string
by_selected_nm_id_req_params_instance = BySelectedNmIDReqParams.from_json(json)
# print the JSON string representation of the object
print(BySelectedNmIDReqParams.to_json())

# convert the object into a dict
by_selected_nm_id_req_params_dict = by_selected_nm_id_req_params_instance.to_dict()
# create an instance of BySelectedNmIDReqParams from a dict
by_selected_nm_id_req_params_from_dict = BySelectedNmIDReqParams.from_dict(by_selected_nm_id_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



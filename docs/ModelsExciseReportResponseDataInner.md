# ModelsExciseReportResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Страна покупателя | [optional] 
**price** | **float** | Цена товара, с НДС | [optional] 
**currency_name_short** | **str** | Валюта | [optional] 
**excise_short** | **str** | Код маркировки | [optional] 
**barcode** | **str** | Баркод | [optional] 
**nm_id** | **int** | Артикул Wildberries | [optional] 
**operation_type_id** | **int** | Тип операции, если есть:    * &#x60;1&#x60; — вывод из оборота   * &#x60;2&#x60; — возврат в оборот  | [optional] 
**fiscal_doc_number** | **int** | Номер фискального документа (чека полного расчёта), если есть | [optional] 
**fiscal_dt** | **str** | Дата фискализации (дата в чеке), если есть, &#x60;ГГГГ-ММ-ДД&#x60; | [optional] 
**fiscal_drive_number** | **str** | Номер фискального накопителя, если есть | [optional] 
**rid** | **int** | &#x60;Rid&#x60;  | [optional] 
**srid** | **str** | &#x60;Srid&#x60;   | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_excise_report_response_data_inner import ModelsExciseReportResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsExciseReportResponseDataInner from a JSON string
models_excise_report_response_data_inner_instance = ModelsExciseReportResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(ModelsExciseReportResponseDataInner.to_json())

# convert the object into a dict
models_excise_report_response_data_inner_dict = models_excise_report_response_data_inner_instance.to_dict()
# create an instance of ModelsExciseReportResponseDataInner from a dict
models_excise_report_response_data_inner_from_dict = ModelsExciseReportResponseDataInner.from_dict(models_excise_report_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



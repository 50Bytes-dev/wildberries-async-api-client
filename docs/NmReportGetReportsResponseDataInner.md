# NmReportGetReportsResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отчёта | [optional] 
**created_at** | **datetime** | Дата и время завершения генерации | [optional] 
**status** | **str** | Статус отчёта:  * &#x60;WAITING&#x60; — в очереди на обработку * &#x60;PROCESSING&#x60; — генерируется * &#x60;SUCCESS —&#x60; готов * &#x60;RETRY&#x60; — ожидает повторной обработки * &#x60;FAILED&#x60; — не получилось сгенерировать, сгенерируйте повторно  | [optional] 
**name** | **str** | Название отчёта | [optional] 
**size** | **int** | Размер отчёта, Б | [optional] 
**start_date** | **date** | Начало периода | [optional] 
**end_date** | **date** | Конец периода | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_get_reports_response_data_inner import NmReportGetReportsResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportGetReportsResponseDataInner from a JSON string
nm_report_get_reports_response_data_inner_instance = NmReportGetReportsResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(NmReportGetReportsResponseDataInner.to_json())

# convert the object into a dict
nm_report_get_reports_response_data_inner_dict = nm_report_get_reports_response_data_inner_instance.to_dict()
# create an instance of NmReportGetReportsResponseDataInner from a dict
nm_report_get_reports_response_data_inner_from_dict = NmReportGetReportsResponseDataInner.from_dict(nm_report_get_reports_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



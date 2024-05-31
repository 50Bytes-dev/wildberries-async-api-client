# BySelectedNmIDReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отчёта в UUID-формате. Генерируется продавцом самостоятельно | 
**report_type** | **str** | Тип отчёта — &#x60;DETAIL_HISTORY_REPORT&#x60; | 
**user_report_name** | **str** | Название отчёта (если не указано, сформируется автоматически) | [optional] 
**params** | [**BySelectedNmIDReqParams**](BySelectedNmIDReqParams.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.by_selected_nm_id_req import BySelectedNmIDReq

# TODO update the JSON string below
json = "{}"
# create an instance of BySelectedNmIDReq from a JSON string
by_selected_nm_id_req_instance = BySelectedNmIDReq.from_json(json)
# print the JSON string representation of the object
print(BySelectedNmIDReq.to_json())

# convert the object into a dict
by_selected_nm_id_req_dict = by_selected_nm_id_req_instance.to_dict()
# create an instance of BySelectedNmIDReq from a dict
by_selected_nm_id_req_from_dict = BySelectedNmIDReq.from_dict(by_selected_nm_id_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GroupedByObjectsBrandsAndTagsReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор отчёта в UUID-формате. Генерируется продавцом самостоятельно | 
**report_type** | **str** | Тип отчёта — &#x60;GROUPED_HISTORY_REPORT&#x60; | 
**user_report_name** | **str** | Название отчёта (если не указано, сформируется автоматически) | [optional] 
**params** | [**GroupedByObjectsBrandsAndTagsReqParams**](GroupedByObjectsBrandsAndTagsReqParams.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.grouped_by_objects_brands_and_tags_req import GroupedByObjectsBrandsAndTagsReq

# TODO update the JSON string below
json = "{}"
# create an instance of GroupedByObjectsBrandsAndTagsReq from a JSON string
grouped_by_objects_brands_and_tags_req_instance = GroupedByObjectsBrandsAndTagsReq.from_json(json)
# print the JSON string representation of the object
print(GroupedByObjectsBrandsAndTagsReq.to_json())

# convert the object into a dict
grouped_by_objects_brands_and_tags_req_dict = grouped_by_objects_brands_and_tags_req_instance.to_dict()
# create an instance of GroupedByObjectsBrandsAndTagsReq from a dict
grouped_by_objects_brands_and_tags_req_from_dict = GroupedByObjectsBrandsAndTagsReq.from_dict(grouped_by_objects_brands_and_tags_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



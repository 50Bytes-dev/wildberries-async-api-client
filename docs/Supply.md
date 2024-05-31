# Supply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Идентификатор поставки | [optional] 
**done** | **bool** | Флаг закрытия поставки | [optional] 
**created_at** | **datetime** | Дата создания поставки (RFC3339) | [optional] 
**closed_at** | **datetime** | Дата закрытия поставки (RFC3339) | [optional] 
**scan_dt** | **datetime** | Дата скана поставки (RFC3339) | [optional] 
**name** | **str** | Наименование поставки | [optional] 
**cargo_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип поставки:&lt;/dt&gt; &lt;dd&gt;0 - признак отсутствует&lt;/dd&gt; &lt;dd&gt;1 - обычная&lt;/dd&gt; &lt;dd&gt;2 - СГТ (Содержит сверхгабаритные товары)&lt;/dd&gt; &lt;dd&gt;3 - КГТ (Содержит крупногабаритные товары). Не используется на данный момент.&lt;/dd&gt; &lt;/dl&gt;  | [optional] 

## Example

```python
from wb_client.models.supply import Supply

# TODO update the JSON string below
json = "{}"
# create an instance of Supply from a JSON string
supply_instance = Supply.from_json(json)
# print the JSON string representation of the object
print(Supply.to_json())

# convert the object into a dict
supply_dict = supply_instance.to_dict()
# create an instance of Supply from a dict
supply_from_dict = Supply.from_dict(supply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



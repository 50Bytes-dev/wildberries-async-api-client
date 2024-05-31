# Office

Данные о складе WB

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Адрес | [optional] 
**name** | **str** | Название | [optional] 
**city** | **str** | Город | [optional] 
**id** | **int** | ID | [optional] 
**longitude** | **float** | Долгота | [optional] 
**latitude** | **float** | Широта | [optional] 
**cargo_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип товара, который принимает склад:&lt;/dt&gt; &lt;dd&gt;1 - обычный&lt;/dd&gt; &lt;dd&gt;2 - СГТ (Сверхгабаритный товар)&lt;/dd&gt; &lt;dd&gt;3 - КГТ (Крупногабаритный товар). Не используется на данный момент.&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**delivery_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип доставки, который принимает склад:&lt;/dt&gt; &lt;dd&gt;1 - доставка на склад Wildberries&lt;/dd&gt; &lt;dd&gt;2 - доставка силами продавца&lt;/dd&gt; &lt;dd&gt;3 - доставка курьером WB&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**selected** | **bool** | Признак того, что склад уже выбран продавцом | [optional] 

## Example

```python
from wb_client.models.office import Office

# TODO update the JSON string below
json = "{}"
# create an instance of Office from a JSON string
office_instance = Office.from_json(json)
# print the JSON string representation of the object
print(Office.to_json())

# convert the object into a dict
office_dict = office_instance.to_dict()
# create an instance of Office from a dict
office_from_dict = Office.from_dict(office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Warehouse

Данные о складе продавца

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Название склада продавца | [optional] 
**office_id** | **int** | ID склада WB | [optional] 
**id** | **int** | ID склада продавца | [optional] 
**cargo_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип товара, который принимает склад:&lt;/dt&gt; &lt;dd&gt;1 - обычный&lt;/dd&gt; &lt;dd&gt;2 - СГТ (Сверхгабаритный товар)&lt;/dd&gt; &lt;dd&gt;3 - КГТ (Крупногабаритный товар). Не используется на данный момент.&lt;/dd&gt; &lt;/dl&gt;  | [optional] 
**delivery_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип доставки, который принимает склад:&lt;/dt&gt; &lt;dd&gt;1 - доставка на склад Wildberries&lt;/dd&gt; &lt;dd&gt;2 - доставка силами продавца&lt;/dd&gt; &lt;dd&gt;3 - доставка курьером WB&lt;/dd&gt; &lt;/dl&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.warehouse import Warehouse

# TODO update the JSON string below
json = "{}"
# create an instance of Warehouse from a JSON string
warehouse_instance = Warehouse.from_json(json)
# print the JSON string representation of the object
print(Warehouse.to_json())

# convert the object into a dict
warehouse_dict = warehouse_instance.to_dict()
# create an instance of Warehouse from a dict
warehouse_from_dict = Warehouse.from_dict(warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



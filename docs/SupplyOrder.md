# SupplyOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Идентификатор сборочного задания в Маркетплейсе | [optional] 
**rid** | **str** | Идентификатор сборочного задания в системе Wildberries | [optional] 
**created_at** | **datetime** | Дата создания сборочного задания (RFC3339) | [optional] 
**warehouse_id** | **int** | Идентификатор склада продавца, на который поступило сборочное задание | [optional] 
**offices** | **List[str]** | Список офисов, куда следует привезти товар | [optional] 
**user** | [**OrderUser**](OrderUser.md) |  | [optional] 
**skus** | **List[str]** | Массив баркодов товара | [optional] 
**price** | **int** | Цена в валюте продажи с учетом всех скидок, умноженная на 100. Код валюты продажи в поле currencyCode. | [optional] 
**converted_price** | **int** | Цена в валюте страны продавца с учетом всех скидок, кроме суммы по WB Кошельку, умноженная на 100. Предоставляется в информационных целях. | [optional] 
**currency_code** | **int** | Код валюты продажи (ISO 4217) | [optional] 
**converted_currency_code** | **int** | Код валюты страны продавца (ISO 4217) | [optional] 
**order_uid** | **str** | Идентификатор транзакции для группировки сборочных заданий. Сборочные задания в одной корзине покупателя будут иметь одинаковый orderUID | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**chrt_id** | **int** | Идентификатор размера товара в системе Wildberries | [optional] 
**article** | **str** | Артикул продавца | [optional] 
**color_code** | **str** | Код цвета (только для колеруемых товаров) | [optional] 
**cargo_type** | **int** | &lt;dl&gt; &lt;dt&gt;Тип товара:&lt;/dt&gt; &lt;dd&gt;1 - обычный&lt;/dd&gt; &lt;dd&gt;2 - СГТ (Сверхгабаритный товар)&lt;/dd&gt; &lt;dd&gt;3 - КГТ (Крупногабаритный товар). Не используется на данный момент.&lt;/dd&gt; &lt;/dl&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.supply_order import SupplyOrder

# TODO update the JSON string below
json = "{}"
# create an instance of SupplyOrder from a JSON string
supply_order_instance = SupplyOrder.from_json(json)
# print the JSON string representation of the object
print(SupplyOrder.to_json())

# convert the object into a dict
supply_order_dict = supply_order_instance.to_dict()
# create an instance of SupplyOrder from a dict
supply_order_from_dict = SupplyOrder.from_dict(supply_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



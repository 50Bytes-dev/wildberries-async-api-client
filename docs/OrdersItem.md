# OrdersItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Дата и время заказа. Это поле соответствует параметру &#x60;dateFrom&#x60; в запросе, если параметр &#x60;flag&#x60;&#x3D;1. Если часовой пояс не указан, то берется Московское время (UTC+3). | [optional] 
**last_change_date** | **datetime** | Дата и время обновления информации в сервисе. Это поле соответствует параметру &#x60;dateFrom&#x60; в запросе, если параметр &#x60;flag&#x60;&#x3D;0 или не указан. Если часовой пояс не указан, то берется Московское время (UTC+3). | [optional] 
**warehouse_name** | **str** | Склад отгрузки | [optional] 
**country_name** | **str** | Страна | [optional] 
**oblast_okrug_name** | **str** | Округ | [optional] 
**region_name** | **str** | Регион | [optional] 
**supplier_article** | **str** | Артикул продавца | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**barcode** | **str** | Баркод | [optional] 
**category** | **str** | Категория | [optional] 
**subject** | **str** | Предмет | [optional] 
**brand** | **str** | Бренд | [optional] 
**tech_size** | **str** | Размер товара | [optional] 
**income_id** | **int** | Номер поставки | [optional] 
**is_supply** | **bool** | Договор поставки | [optional] 
**is_realization** | **bool** | Договор реализации | [optional] 
**total_price** | **float** | Цена без скидок | [optional] 
**discount_percent** | **int** | Скидка продавца | [optional] 
**spp** | **float** | Скидка WB | [optional] 
**finished_price** | **float** | Цена с учетом всех скидок, кроме суммы по WB Кошельку | [optional] 
**price_with_disc** | **float** | Цена со скидкой продавца (&#x3D; &#x60;totalPrice&#x60; * (1 - &#x60;discountPercent&#x60;/100)) | [optional] 
**is_cancel** | **bool** | Отмена заказа. true - заказ отменен | [optional] 
**cancel_date** | **datetime** | Дата и время отмены заказа. Если заказ не был отменен, то \&quot;0001-01-01T00:00:00\&quot;.Если часовой пояс не указан, то берется Московское время UTC+3. | [optional] 
**order_type** | **str** | Тип заказа &lt;ul&gt; &lt;li&gt; &#x60;Клиентский&#x60; — заказ, поступивший от покупателя &lt;li&gt; &#x60;Возврат Брака&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Принудительный возврат&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Возврат обезлички&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Возврат Неверного Вложения&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Возврат Продавца&#x60; — возврат товара продавцу &lt;/ul&gt;  | [optional] 
**sticker** | **str** | Идентификатор стикера | [optional] 
**g_number** | **str** | Номер заказа | [optional] 
**srid** | **str** | Уникальный идентификатор заказа.&lt;br&gt; Примечание для использующих API Маркетплейс: &#x60;srid&#x60; равен &#x60;rid&#x60; в ответах методов сборочных заданий.  | [optional] 

## Example

```python
from wildberries_async_api_client.models.orders_item import OrdersItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersItem from a JSON string
orders_item_instance = OrdersItem.from_json(json)
# print the JSON string representation of the object
print(OrdersItem.to_json())

# convert the object into a dict
orders_item_dict = orders_item_instance.to_dict()
# create an instance of OrdersItem from a dict
orders_item_from_dict = OrdersItem.from_dict(orders_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



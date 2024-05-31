# SalesItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Дата и время продажи. Это поле соответствует параметру &#x60;dateFrom&#x60; в запросе, если параметр &#x60;flag&#x60;&#x3D;1. Если часовой пояс не указан, то берется Московское время (UTC+3). | [optional] 
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
**payment_sale_amount** | **int** | Оплачено с WB Кошелька | [optional] 
**for_pay** | **float** | К перечислению продавцу | [optional] 
**finished_price** | **float** | Фактическая цена с учетом всех скидок (к взиманию с покупателя) | [optional] 
**price_with_disc** | **float** | Цена со скидкой продавца, от которой считается сумма к перечислению продавцу &#x60;forPay&#x60; (&#x3D; &#x60;totalPrice&#x60; * (1 - &#x60;discountPercent&#x60;/100)) | [optional] 
**sale_id** | **str** | Уникальный идентификатор продажи/возврата &lt;ul&gt;  &lt;li&gt; &#x60;S**********&#x60; — продажа  &lt;li&gt; &#x60;R**********&#x60; — возврат (на склад WB)  &lt;/ul&gt;  | [optional] 
**order_type** | **str** | Тип заказа &lt;ul&gt; &lt;li&gt; &#x60;Клиентский&#x60; — заказ, поступивший от покупателя &lt;li&gt; &#x60;Возврат Брака&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Принудительный возврат&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Возврат обезлички&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Возврат Неверного Вложения&#x60; — возврат товара продавцу &lt;li&gt; &#x60;Возврат Продавца&#x60; — возврат товара продавцу &lt;/ul&gt;  | [optional] 
**sticker** | **str** | Идентификатор стикера | [optional] 
**g_number** | **str** | Номер заказа | [optional] 
**srid** | **str** | Уникальный идентификатор заказа.&lt;br&gt; Примечание для использующих API Маркетплейс: &#x60;srid&#x60; равен &#x60;rid&#x60; в ответах методов сборочных заданий.  | [optional] 

## Example

```python
from wildberries_async_api_client.models.sales_item import SalesItem

# TODO update the JSON string below
json = "{}"
# create an instance of SalesItem from a JSON string
sales_item_instance = SalesItem.from_json(json)
# print the JSON string representation of the object
print(SalesItem.to_json())

# convert the object into a dict
sales_item_dict = sales_item_instance.to_dict()
# create an instance of SalesItem from a dict
sales_item_from_dict = SalesItem.from_dict(sales_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



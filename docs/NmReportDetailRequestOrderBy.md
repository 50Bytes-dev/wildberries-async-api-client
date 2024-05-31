# NmReportDetailRequestOrderBy

Параметры сортировки. Если не указано, то по умолчанию используется значение \"openCard\" и сортировка по убыванию. <dl> <dt>Все виды сортировки <code>field</code>:</dt> <dd><code>openCard </code> — по открытию карточки (переход на страницу товара)</dd> <dd><code>addToCart </code> — по добавлениям в корзину</dd> <dd><code>orders </code> — по кол-ву заказов</dd> <dd><code>avgRubPrice </code> — по средней цене в рублях</dd> <dd><code>ordersSumRub </code> — по сумме заказов в рублях</dd> <dd><code>stockMpQty </code> — по кол-ву остатков маркетплейса шт.</dd> <dd><code>stockWbQty </code> — по кол-ву остатков на складе шт.</dd> <dd><code>cancelSumRub </code> — сумме возвратов в рублях</dd> <dd><code>cancelCount </code> — по кол-ву возвратов</dd> <dd><code>buyoutCount </code> — по кол-ву выкупов</dd> <dd><code>buyoutSumRub </code> — по сумме выкупов</dd> </dl> 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Вид сортировки | [optional] 
**mode** | **str** | &#x60;asc&#x60; — по возрастанию, &#x60;desc&#x60; — по убыванию                  | [optional] 

## Example

```python
from wildberries_async_api_client.models.nm_report_detail_request_order_by import NmReportDetailRequestOrderBy

# TODO update the JSON string below
json = "{}"
# create an instance of NmReportDetailRequestOrderBy from a JSON string
nm_report_detail_request_order_by_instance = NmReportDetailRequestOrderBy.from_json(json)
# print the JSON string representation of the object
print(NmReportDetailRequestOrderBy.to_json())

# convert the object into a dict
nm_report_detail_request_order_by_dict = nm_report_detail_request_order_by_instance.to_dict()
# create an instance of NmReportDetailRequestOrderBy from a dict
nm_report_detail_request_order_by_from_dict = NmReportDetailRequestOrderBy.from_dict(nm_report_detail_request_order_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



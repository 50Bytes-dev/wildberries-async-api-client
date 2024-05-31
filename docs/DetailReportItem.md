# DetailReportItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realizationreport_id** | **int** | Номер отчёта | [optional] 
**date_from** | **datetime** | Дата начала отчётного периода | [optional] 
**date_to** | **datetime** | Дата конца отчётного периода | [optional] 
**create_dt** | **datetime** | Дата формирования отчёта | [optional] 
**currency_name** | **str** | Валюта отчёта | [optional] 
**suppliercontract_code** | **object** | Договор | [optional] 
**rrd_id** | **int** | Номер строки | [optional] 
**gi_id** | **int** | Номер поставки | [optional] 
**subject_name** | **str** | Предмет | [optional] 
**nm_id** | **int** | Артикул WB | [optional] 
**brand_name** | **str** | Бренд | [optional] 
**sa_name** | **str** | Артикул продавца | [optional] 
**ts_name** | **str** | Размер | [optional] 
**barcode** | **str** | Баркод | [optional] 
**doc_type_name** | **str** | Тип документа | [optional] 
**quantity** | **int** | Количество | [optional] 
**retail_price** | **float** | Цена розничная | [optional] 
**retail_amount** | **float** | Сумма продаж (возвратов) | [optional] 
**sale_percent** | **int** | Согласованная скидка | [optional] 
**commission_percent** | **float** | Процент комиссии | [optional] 
**office_name** | **str** | Склад | [optional] 
**supplier_oper_name** | **str** | Обоснование для оплаты | [optional] 
**order_dt** | **datetime** | Дата заказа. &lt;br&gt;Присылается с явным указанием часового пояса | [optional] 
**sale_dt** | **datetime** | Дата продажи. &lt;br&gt;Присылается с явным указанием часового пояса | [optional] 
**rr_dt** | **datetime** | Дата операции. &lt;br&gt; Присылается с явным указанием часового пояса | [optional] 
**shk_id** | **int** | Штрих-код | [optional] 
**retail_price_withdisc_rub** | **float** | Цена розничная с учетом согласованной скидки | [optional] 
**delivery_amount** | **int** | Количество доставок | [optional] 
**return_amount** | **int** | Количество возвратов | [optional] 
**delivery_rub** | **float** | Стоимость логистики | [optional] 
**gi_box_type_name** | **str** | Тип коробов | [optional] 
**product_discount_for_report** | **float** | Согласованный продуктовый дисконт | [optional] 
**supplier_promo** | **float** | Промокод | [optional] 
**rid** | **int** | Уникальный идентификатор заказа | [optional] 
**ppvz_spp_prc** | **float** | Скидка постоянного покупателя | [optional] 
**ppvz_kvw_prc_base** | **float** | Размер кВВ без НДС, % базовый | [optional] 
**ppvz_kvw_prc** | **float** | Итоговый кВВ без НДС, % | [optional] 
**sup_rating_prc_up** | **float** | Размер снижения кВВ из-за рейтинга | [optional] 
**is_kgvp_v2** | **float** | Размер снижения кВВ из-за акции | [optional] 
**ppvz_sales_commission** | **float** | Вознаграждение с продаж до вычета услуг поверенного, без НДС | [optional] 
**ppvz_for_pay** | **float** | К перечислению продавцу за реализованный товар | [optional] 
**ppvz_reward** | **float** | Возмещение за выдачу и возврат товаров на ПВЗ | [optional] 
**acquiring_fee** | **float** | Возмещение издержек по эквайрингу. &lt;br&gt; Издержки WB за услуги эквайринга: вычитаются из вознаграждения WB и не влияют на доход продавца.  | [optional] 
**acquiring_bank** | **str** | Наименование банка-эквайера | [optional] 
**ppvz_vw** | **float** | Вознаграждение WB без НДС | [optional] 
**ppvz_vw_nds** | **float** | НДС с вознаграждения WB | [optional] 
**ppvz_office_id** | **int** | Номер офиса | [optional] 
**ppvz_office_name** | **str** | Наименование офиса доставки | [optional] 
**ppvz_supplier_id** | **int** | Номер партнера | [optional] 
**ppvz_supplier_name** | **str** | Партнер | [optional] 
**ppvz_inn** | **str** | ИНН партнера | [optional] 
**declaration_number** | **str** | Номер таможенной декларации | [optional] 
**bonus_type_name** | **str** | Обоснование штрафов и доплат. &lt;br&gt;Поле будет в ответе при наличии значения | [optional] 
**sticker_id** | **str** | Цифровое значение стикера, который клеится на товар в процессе сборки заказа по схеме \&quot;Маркетплейс\&quot; | [optional] 
**site_country** | **str** | Страна продажи | [optional] 
**penalty** | **float** | Штрафы | [optional] 
**additional_payment** | **float** | Доплаты | [optional] 
**rebill_logistic_cost** | **float** | Возмещение издержек по перевозке. Поле будет в ответе при наличии значения | [optional] 
**rebill_logistic_org** | **str** | Организатор перевозки. Поле будет в ответе при наличии значения | [optional] 
**kiz** | **str** | Код маркировки. &lt;br&gt; Поле будет в ответе при наличии значения | [optional] 
**storage_fee** | **float** | Стоимость хранения | [optional] 
**deduction** | **float** | Прочие удержания/выплаты | [optional] 
**acceptance** | **float** | Стоимость платной приёмки | [optional] 
**srid** | **str** | Уникальный идентификатор заказа.  Примечание для использующих API Marketplace: &#x60;srid&#x60; равен &#x60;rid&#x60; в ответах методов сборочных заданий.  | [optional] 
**report_type** | **int** | Тип отчёта:    * &#x60;1&#x60; — стандартный   * &#x60;2&#x60; — для уведомления о выкупе  | [optional] 

## Example

```python
from wildberries_async_api_client.models.detail_report_item import DetailReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of DetailReportItem from a JSON string
detail_report_item_instance = DetailReportItem.from_json(json)
# print the JSON string representation of the object
print(DetailReportItem.to_json())

# convert the object into a dict
detail_report_item_dict = detail_report_item_instance.to_dict()
# create an instance of DetailReportItem from a dict
detail_report_item_from_dict = DetailReportItem.from_dict(detail_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



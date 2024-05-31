# ResponsePaidStorageInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Дата, за которую был расчёт или перерасчёт | [optional] 
**log_warehouse_coef** | **float** | Коэффициент логистики и хранения | [optional] 
**office_id** | **int** | ID склада | [optional] 
**warehouse** | **str** | Название склада | [optional] 
**warehouse_coef** | **float** | Коэффициент склада | [optional] 
**gi_id** | **int** | ID поставки | [optional] 
**chrt_id** | **int** | Идентификатор размера для этого артикула Wildberries | [optional] 
**size** | **str** | Размер (&#x60;techSize&#x60; в карточке товара) | [optional] 
**barcode** | **str** | Баркод | [optional] 
**subject** | **str** | Предмет | [optional] 
**brand** | **str** | Бренд | [optional] 
**vendor_code** | **str** | Артикул продавца | [optional] 
**nm_id** | **int** | Артикул Wildberries | [optional] 
**volume** | **float** | Объём товара | [optional] 
**calc_type** | **str** | Способ расчёта | [optional] 
**warehouse_price** | **float** | Сумма хранения | [optional] 
**barcodes_count** | **int** | Количество единиц товара (штук), подлежащих тарифицированию за расчётные сутки | [optional] 
**pallet_place_code** | **int** | Код паллетоместа | [optional] 
**pallet_count** | **float** | Количество паллет | [optional] 
**original_date** | **str** | Если был перерасчёт, это дата первоначального расчёта. Если перерасчёта не было, совпадает с &#x60;date&#x60; | [optional] 
**loyalty_discount** | **float** | Скидка программы лояльности, ₽ | [optional] 
**tariff_fix_date** | **str** | Дата фиксации тарифа | [optional] 
**tariff_lower_date** | **str** | Дата понижения тарифа | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_paid_storage_inner import ResponsePaidStorageInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsePaidStorageInner from a JSON string
response_paid_storage_inner_instance = ResponsePaidStorageInner.from_json(json)
# print the JSON string representation of the object
print(ResponsePaidStorageInner.to_json())

# convert the object into a dict
response_paid_storage_inner_dict = response_paid_storage_inner_instance.to_dict()
# create an instance of ResponsePaidStorageInner from a dict
response_paid_storage_inner_from_dict = ResponsePaidStorageInner.from_dict(response_paid_storage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



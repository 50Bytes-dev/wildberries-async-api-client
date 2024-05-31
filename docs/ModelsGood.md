# ModelsGood


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Суммарное количество товаров, планируемых для поставки. Максимум 999999  | [optional] 
**barcode** | **str** | Баркод из карточки товара | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_good import ModelsGood

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsGood from a JSON string
models_good_instance = ModelsGood.from_json(json)
# print the JSON string representation of the object
print(ModelsGood.to_json())

# convert the object into a dict
models_good_dict = models_good_instance.to_dict()
# create an instance of ModelsGood from a dict
models_good_from_dict = ModelsGood.from_dict(models_good_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



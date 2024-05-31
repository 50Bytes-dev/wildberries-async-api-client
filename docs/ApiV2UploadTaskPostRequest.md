# ApiV2UploadTaskPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Good]**](Good.md) | Товары, цены и скидки для них. Максимум 1 000 товаров. Цена и скидка не могут быть пустыми одновременно. &lt;br&gt;&lt;br&gt; Если новая цена со скидкой будет хотя бы в 3 раза меньше старой, она попадёт [в карантин](https://seller.wildberries.ru/discount-and-prices/quarantine) и товар будет продаваться по старой цене. Ошибка об этом будет в ответах методов [Состояния загрузок](./#tag/Sostoyaniya-zagruzok) &lt;br&gt;&lt;br&gt; Вы можете изменить цену или скидку с помощью API либо вывести товар из карантина [в личном кабинете](https://seller.wildberries.ru/discount-and-prices/quarantine)  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_upload_task_post_request import ApiV2UploadTaskPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2UploadTaskPostRequest from a JSON string
api_v2_upload_task_post_request_instance = ApiV2UploadTaskPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV2UploadTaskPostRequest.to_json())

# convert the object into a dict
api_v2_upload_task_post_request_dict = api_v2_upload_task_post_request_instance.to_dict()
# create an instance of ApiV2UploadTaskPostRequest from a dict
api_v2_upload_task_post_request_from_dict = ApiV2UploadTaskPostRequest.from_dict(api_v2_upload_task_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



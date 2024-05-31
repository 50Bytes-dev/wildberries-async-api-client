# ApiV2HistoryTasksGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SupplierTaskMetadata**](SupplierTaskMetadata.md) |  | [optional] 
**error** | **bool** | Флаг ошибки | [optional] 
**error_text** | **str** | Текст ошибки  &lt;blockquote class&#x3D;\&quot;spoiler\&quot;&gt;   &lt;p class&#x3D;\&quot;descr\&quot;&gt;Ошибка &lt;code&gt;The product is in quarantine&lt;/code&gt; возникает, если новая цена со скидкой хотя бы в 3 раза меньше старой. Вы можете изменить цену или скидку с помощью API либо вывести товар из карантина &lt;a href&#x3D;\&quot;https://seller.wildberries.ru/discount-and-prices/quarantine\&quot;&gt;в личном кабинете&lt;/a&gt;&lt;/p&gt; &lt;/blockquote&gt;  | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_history_tasks_get200_response import ApiV2HistoryTasksGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2HistoryTasksGet200Response from a JSON string
api_v2_history_tasks_get200_response_instance = ApiV2HistoryTasksGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiV2HistoryTasksGet200Response.to_json())

# convert the object into a dict
api_v2_history_tasks_get200_response_dict = api_v2_history_tasks_get200_response_instance.to_dict()
# create an instance of ApiV2HistoryTasksGet200Response from a dict
api_v2_history_tasks_get200_response_from_dict = ApiV2HistoryTasksGet200Response.from_dict(api_v2_history_tasks_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



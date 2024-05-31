# ApiV2HistoryGoodsTaskGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **int** | ID загрузки | [optional] 
**history_goods** | [**List[GoodHistory]**](GoodHistory.md) | Информация о товарах в загрузке | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v2_history_goods_task_get200_response_data import ApiV2HistoryGoodsTaskGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2HistoryGoodsTaskGet200ResponseData from a JSON string
api_v2_history_goods_task_get200_response_data_instance = ApiV2HistoryGoodsTaskGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV2HistoryGoodsTaskGet200ResponseData.to_json())

# convert the object into a dict
api_v2_history_goods_task_get200_response_data_dict = api_v2_history_goods_task_get200_response_data_instance.to_dict()
# create an instance of ApiV2HistoryGoodsTaskGet200ResponseData from a dict
api_v2_history_goods_task_get200_response_data_from_dict = ApiV2HistoryGoodsTaskGet200ResponseData.from_dict(api_v2_history_goods_task_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



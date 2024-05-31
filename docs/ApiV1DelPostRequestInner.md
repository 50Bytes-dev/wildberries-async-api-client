# ApiV1DelPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm** | **int** | Идентификатор товара (&#x60;nmId&#x60;), у которого необходимо удалить рекомендацию | 
**recom** | **List[int]** | Список идентификаторов товаров (&#x60;nmId&#x60;), которые необходимо удалить из рекомендуемых | 

## Example

```python
from wildberries_async_api_client.models.api_v1_del_post_request_inner import ApiV1DelPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1DelPostRequestInner from a JSON string
api_v1_del_post_request_inner_instance = ApiV1DelPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1DelPostRequestInner.to_json())

# convert the object into a dict
api_v1_del_post_request_inner_dict = api_v1_del_post_request_inner_instance.to_dict()
# create an instance of ApiV1DelPostRequestInner from a dict
api_v1_del_post_request_inner_from_dict = ApiV1DelPostRequestInner.from_dict(api_v1_del_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



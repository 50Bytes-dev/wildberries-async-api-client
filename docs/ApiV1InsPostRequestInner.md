# ApiV1InsPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm** | **int** | Идентификатор товара (&#x60;nmId&#x60;), к которому добавляется рекомендация | 
**recom** | **List[int]** | Список идентификаторов товаров (&#x60;nmId&#x60;), которые необходимо добавить в рекомендуемые | 

## Example

```python
from wildberries_async_api_client.models.api_v1_ins_post_request_inner import ApiV1InsPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1InsPostRequestInner from a JSON string
api_v1_ins_post_request_inner_instance = ApiV1InsPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1InsPostRequestInner.to_json())

# convert the object into a dict
api_v1_ins_post_request_inner_dict = api_v1_ins_post_request_inner_instance.to_dict()
# create an instance of ApiV1InsPostRequestInner from a dict
api_v1_ins_post_request_inner_from_dict = ApiV1InsPostRequestInner.from_dict(api_v1_ins_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1SetPostRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm** | **int** | Артикул WB (&#x60;nmId&#x60;), которому передается рекомендация | 
**recom** | **List[int]** | Список артикулов WB (&#x60;nmId&#x60;), которые необходимо передать в рекомендуемые. | 

## Example

```python
from wildberries_async_api_client.models.api_v1_set_post_request_inner import ApiV1SetPostRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1SetPostRequestInner from a JSON string
api_v1_set_post_request_inner_instance = ApiV1SetPostRequestInner.from_json(json)
# print the JSON string representation of the object
print(ApiV1SetPostRequestInner.to_json())

# convert the object into a dict
api_v1_set_post_request_inner_dict = api_v1_set_post_request_inner_instance.to_dict()
# create an instance of ApiV1SetPostRequestInner from a dict
api_v1_set_post_request_inner_from_dict = ApiV1SetPostRequestInner.from_dict(api_v1_set_post_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



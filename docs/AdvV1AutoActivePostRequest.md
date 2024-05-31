# AdvV1AutoActivePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recom** | **bool** | Рекомендации на главной (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены) | [optional] 
**booster** | **bool** | Поиск/Каталог (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены) | [optional] 
**carousel** | **bool** | Карточка товара (&#x60;false&#x60; - отключены, &#x60;true&#x60; - включены) | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_auto_active_post_request import AdvV1AutoActivePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AutoActivePostRequest from a JSON string
adv_v1_auto_active_post_request_instance = AdvV1AutoActivePostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1AutoActivePostRequest.to_json())

# convert the object into a dict
adv_v1_auto_active_post_request_dict = adv_v1_auto_active_post_request_instance.to_dict()
# create an instance of AdvV1AutoActivePostRequest from a dict
adv_v1_auto_active_post_request_from_dict = AdvV1AutoActivePostRequest.from_dict(adv_v1_auto_active_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



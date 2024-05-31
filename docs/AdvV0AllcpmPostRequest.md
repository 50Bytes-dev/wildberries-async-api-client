# AdvV0AllcpmPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**param** | **List[int]** | Массив параметров запроса, по которым будет получен список ставок активных кампаний: должен быть значением &#x60;menuId&#x60; (для кампании в каталоге), &#x60;subjectId&#x60; (для кампании в поиске и рекомендациях) или &#x60;setId&#x60; (для кампании в карточке товара).  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v0_allcpm_post_request import AdvV0AllcpmPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV0AllcpmPostRequest from a JSON string
adv_v0_allcpm_post_request_instance = AdvV0AllcpmPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV0AllcpmPostRequest.to_json())

# convert the object into a dict
adv_v0_allcpm_post_request_dict = adv_v0_allcpm_post_request_instance.to_dict()
# create an instance of AdvV0AllcpmPostRequest from a dict
adv_v0_allcpm_post_request_from_dict = AdvV0AllcpmPostRequest.from_dict(adv_v0_allcpm_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AdvV1AdvertStartPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | ID медиакампании | 
**reason** | **str** | Описание причины запуска | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_advert_start_post_request import AdvV1AdvertStartPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AdvertStartPostRequest from a JSON string
adv_v1_advert_start_post_request_instance = AdvV1AdvertStartPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1AdvertStartPostRequest.to_json())

# convert the object into a dict
adv_v1_advert_start_post_request_dict = adv_v1_advert_start_post_request_instance.to_dict()
# create an instance of AdvV1AdvertStartPostRequest from a dict
adv_v1_advert_start_post_request_from_dict = AdvV1AdvertStartPostRequest.from_dict(adv_v1_advert_start_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



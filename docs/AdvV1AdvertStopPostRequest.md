# AdvV1AdvertStopPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advert_id** | **int** | ID медиакампании | 
**reason** | **str** | Описание причины завершения | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_advert_stop_post_request import AdvV1AdvertStopPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1AdvertStopPostRequest from a JSON string
adv_v1_advert_stop_post_request_instance = AdvV1AdvertStopPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV1AdvertStopPostRequest.to_json())

# convert the object into a dict
adv_v1_advert_stop_post_request_dict = adv_v1_advert_stop_post_request_instance.to_dict()
# create an instance of AdvV1AdvertStopPostRequest from a dict
adv_v1_advert_stop_post_request_from_dict = AdvV1AdvertStopPostRequest.from_dict(adv_v1_advert_stop_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



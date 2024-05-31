# ApiV3PassesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Имя водителя | 
**last_name** | **str** | Фамилия водителя | 
**car_model** | **str** | Марка машины | 
**car_number** | **str** | Номер машины | 
**office_id** | **int** | ID склада | 

## Example

```python
from wb_client.models.api_v3_passes_post_request import ApiV3PassesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3PassesPostRequest from a JSON string
api_v3_passes_post_request_instance = ApiV3PassesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3PassesPostRequest.to_json())

# convert the object into a dict
api_v3_passes_post_request_dict = api_v3_passes_post_request_instance.to_dict()
# create an instance of ApiV3PassesPostRequest from a dict
api_v3_passes_post_request_from_dict = ApiV3PassesPostRequest.from_dict(api_v3_passes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



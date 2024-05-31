# ApiV3PassesPassIdPutRequest


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
from wildberries_async_api_client.models.api_v3_passes_pass_id_put_request import ApiV3PassesPassIdPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV3PassesPassIdPutRequest from a JSON string
api_v3_passes_pass_id_put_request_instance = ApiV3PassesPassIdPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiV3PassesPassIdPutRequest.to_json())

# convert the object into a dict
api_v3_passes_pass_id_put_request_dict = api_v3_passes_pass_id_put_request_instance.to_dict()
# create an instance of ApiV3PassesPassIdPutRequest from a dict
api_v3_passes_pass_id_put_request_from_dict = ApiV3PassesPassIdPutRequest.from_dict(api_v3_passes_pass_id_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



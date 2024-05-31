# AdvV1CountGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** | Общее количество медиакампаний всех статусов и типов | [optional] 
**adverts** | [**AdvV1CountGet200ResponseAdverts**](AdvV1CountGet200ResponseAdverts.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.adv_v1_count_get200_response import AdvV1CountGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV1CountGet200Response from a JSON string
adv_v1_count_get200_response_instance = AdvV1CountGet200Response.from_json(json)
# print the JSON string representation of the object
print(AdvV1CountGet200Response.to_json())

# convert the object into a dict
adv_v1_count_get200_response_dict = adv_v1_count_get200_response_instance.to_dict()
# create an instance of AdvV1CountGet200Response from a dict
adv_v1_count_get200_response_from_dict = AdvV1CountGet200Response.from_dict(adv_v1_count_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



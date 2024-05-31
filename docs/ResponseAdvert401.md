# ResponseAdvert401


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**rejected** | **str** |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.response_advert401 import ResponseAdvert401

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseAdvert401 from a JSON string
response_advert401_instance = ResponseAdvert401.from_json(json)
# print the JSON string representation of the object
print(ResponseAdvert401.to_json())

# convert the object into a dict
response_advert401_dict = response_advert401_instance.to_dict()
# create an instance of ResponseAdvert401 from a dict
response_advert401_from_dict = ResponseAdvert401.from_dict(response_advert401_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



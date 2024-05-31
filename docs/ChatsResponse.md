# ChatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[Chat]**](Chat.md) |  | [optional] 
**errors** | **object** | Ошибки, если есть | [optional] 

## Example

```python
from wildberries_async_api_client.models.chats_response import ChatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatsResponse from a JSON string
chats_response_instance = ChatsResponse.from_json(json)
# print the JSON string representation of the object
print(ChatsResponse.to_json())

# convert the object into a dict
chats_response_dict = chats_response_instance.to_dict()
# create an instance of ChatsResponse from a dict
chats_response_from_dict = ChatsResponse.from_dict(chats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



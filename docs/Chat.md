# Chat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** | ID чата | [optional] 
**reply_sign** | **str** | Подпись чата. Требуется при [отправке сообщения](./#/paths/~1api~1v1~1seller~1message/post)  | [optional] 
**client_id** | **str** | ID покупателя | [optional] 
**client_name** | **str** | Имя покупателя | [optional] 

## Example

```python
from wildberries_async_api_client.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print(Chat.to_json())

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_from_dict = Chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



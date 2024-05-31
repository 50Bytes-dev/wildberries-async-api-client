# EventMessage

Данные сообщения

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**EventAttachments**](EventAttachments.md) |  | [optional] 
**text** | **str** | Текст сообщения | [optional] 

## Example

```python
from wildberries_async_api_client.models.event_message import EventMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EventMessage from a JSON string
event_message_instance = EventMessage.from_json(json)
# print the JSON string representation of the object
print(EventMessage.to_json())

# convert the object into a dict
event_message_dict = event_message_instance.to_dict()
# create an instance of EventMessage from a dict
event_message_from_dict = EventMessage.from_dict(event_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



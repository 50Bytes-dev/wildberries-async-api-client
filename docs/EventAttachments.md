# EventAttachments

Вложения

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**good_card** | [**GoodCard**](GoodCard.md) |  | [optional] 
**files** | [**List[File]**](File.md) | Файлы | [optional] 
**images** | [**List[Image]**](Image.md) | Изображения | [optional] 

## Example

```python
from wildberries_async_api_client.models.event_attachments import EventAttachments

# TODO update the JSON string below
json = "{}"
# create an instance of EventAttachments from a JSON string
event_attachments_instance = EventAttachments.from_json(json)
# print the JSON string representation of the object
print(EventAttachments.to_json())

# convert the object into a dict
event_attachments_dict = event_attachments_instance.to_dict()
# create an instance of EventAttachments from a dict
event_attachments_from_dict = EventAttachments.from_dict(event_attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



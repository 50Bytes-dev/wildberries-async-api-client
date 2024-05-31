# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** | ID чата | [optional] 
**event_id** | **str** | ID события | [optional] 
**event_type** | [**EventType**](EventType.md) |  | [optional] 
**is_new_chat** | **bool** | Признак нового чата: - &#x60;false&#x60; — чат не новый  - &#x60;true&#x60; — чат новый  | [optional] 
**message** | [**EventMessage**](EventMessage.md) |  | [optional] 
**refund** | [**Refund**](Refund.md) |  | [optional] 
**source** | **str** | Источник отправки сообщения:  - &#x60;seller-portal&#x60; — портал продавцов  - &#x60;seller-public-api&#x60; — API Чата с покупателями   - &#x60;rusite&#x60; — портал покупателей  | [optional] 
**add_timestamp** | **int** | Время появления события на сервере. Формат Unix timestamp | [optional] 
**add_time** | **str** | Время появления события на сервере в UTC | [optional] 
**reply_sign** | **str** | Подпись чата. Доступна только при &#x60;\&quot;isNewChat\&quot;: true&#x60;. Требуется при [отправке сообщения](./#/paths/~1api~1v1~1seller~1message/post)  | [optional] 
**sender** | [**Sender**](Sender.md) |  | [optional] 
**client_id** | **str** | ID покупателя | [optional] 
**client_name** | **str** | Имя покупателя | [optional] 

## Example

```python
from wildberries_async_api_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



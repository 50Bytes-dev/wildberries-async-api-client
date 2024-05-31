# MessageResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_time** | **int** | Время загрузки | [optional] 
**chat_id** | **str** | ID чата | [optional] 

## Example

```python
from wildberries_async_api_client.models.message_response_result import MessageResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of MessageResponseResult from a JSON string
message_response_result_instance = MessageResponseResult.from_json(json)
# print the JSON string representation of the object
print(MessageResponseResult.to_json())

# convert the object into a dict
message_response_result_dict = message_response_result_instance.to_dict()
# create an instance of MessageResponseResult from a dict
message_response_result_from_dict = MessageResponseResult.from_dict(message_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



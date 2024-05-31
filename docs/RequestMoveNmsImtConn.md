# RequestMoveNmsImtConn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_imt** | **int** | Существующий у продавца &#x60;imtID&#x60;, под которым необходимо объединить НМ | 
**nm_ids** | **List[int]** | &#x60;nmID&#x60;, которые необходимо объединить (максимум 30)  | 

## Example

```python
from wildberries_async_api_client.models.request_move_nms_imt_conn import RequestMoveNmsImtConn

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMoveNmsImtConn from a JSON string
request_move_nms_imt_conn_instance = RequestMoveNmsImtConn.from_json(json)
# print the JSON string representation of the object
print(RequestMoveNmsImtConn.to_json())

# convert the object into a dict
request_move_nms_imt_conn_dict = request_move_nms_imt_conn_instance.to_dict()
# create an instance of RequestMoveNmsImtConn from a dict
request_move_nms_imt_conn_from_dict = RequestMoveNmsImtConn.from_dict(request_move_nms_imt_conn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



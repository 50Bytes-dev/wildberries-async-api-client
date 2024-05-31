# RequestMoveNmsImtDisconn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_ids** | **List[int]** | &#x60;nmID&#x60;, которые необходимо разъединить (max 30) | 

## Example

```python
from wildberries_async_api_client.models.request_move_nms_imt_disconn import RequestMoveNmsImtDisconn

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMoveNmsImtDisconn from a JSON string
request_move_nms_imt_disconn_instance = RequestMoveNmsImtDisconn.from_json(json)
# print the JSON string representation of the object
print(RequestMoveNmsImtDisconn.to_json())

# convert the object into a dict
request_move_nms_imt_disconn_dict = request_move_nms_imt_disconn_instance.to_dict()
# create an instance of RequestMoveNmsImtDisconn from a dict
request_move_nms_imt_disconn_from_dict = RequestMoveNmsImtDisconn.from_dict(request_move_nms_imt_disconn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



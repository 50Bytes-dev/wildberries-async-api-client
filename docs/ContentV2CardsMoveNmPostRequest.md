# ContentV2CardsMoveNmPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_imt** | **int** | Существующий у продавца &#x60;imtID&#x60;, под которым необходимо объединить НМ | 
**nm_ids** | **List[int]** | &#x60;nmID&#x60;, которые необходимо разъединить (max 30) | 

## Example

```python
from wildberries_async_api_client.models.content_v2_cards_move_nm_post_request import ContentV2CardsMoveNmPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2CardsMoveNmPostRequest from a JSON string
content_v2_cards_move_nm_post_request_instance = ContentV2CardsMoveNmPostRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV2CardsMoveNmPostRequest.to_json())

# convert the object into a dict
content_v2_cards_move_nm_post_request_dict = content_v2_cards_move_nm_post_request_instance.to_dict()
# create an instance of ContentV2CardsMoveNmPostRequest from a dict
content_v2_cards_move_nm_post_request_from_dict = ContentV2CardsMoveNmPostRequest.from_dict(content_v2_cards_move_nm_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RequestWithDateInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID кампании | [optional] 
**dates** | **List[date]** | Даты, за которые необходимо выдать информацию. | [optional] 

## Example

```python
from wildberries_async_api_client.models.request_with_date_inner import RequestWithDateInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestWithDateInner from a JSON string
request_with_date_inner_instance = RequestWithDateInner.from_json(json)
# print the JSON string representation of the object
print(RequestWithDateInner.to_json())

# convert the object into a dict
request_with_date_inner_dict = request_with_date_inner_instance.to_dict()
# create an instance of RequestWithDateInner from a dict
request_with_date_inner_from_dict = RequestWithDateInner.from_dict(request_with_date_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



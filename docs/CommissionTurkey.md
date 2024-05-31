# CommissionTurkey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**List[CommissionTurkeyReportInner]**](CommissionTurkeyReportInner.md) | Список комиссий | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_turkey import CommissionTurkey

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionTurkey from a JSON string
commission_turkey_instance = CommissionTurkey.from_json(json)
# print the JSON string representation of the object
print(CommissionTurkey.to_json())

# convert the object into a dict
commission_turkey_dict = commission_turkey_instance.to_dict()
# create an instance of CommissionTurkey from a dict
commission_turkey_from_dict = CommissionTurkey.from_dict(commission_turkey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



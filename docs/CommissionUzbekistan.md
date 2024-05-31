# CommissionUzbekistan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**List[CommissionUzbekistanReportInner]**](CommissionUzbekistanReportInner.md) | Список комиссий | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_uzbekistan import CommissionUzbekistan

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionUzbekistan from a JSON string
commission_uzbekistan_instance = CommissionUzbekistan.from_json(json)
# print the JSON string representation of the object
print(CommissionUzbekistan.to_json())

# convert the object into a dict
commission_uzbekistan_dict = commission_uzbekistan_instance.to_dict()
# create an instance of CommissionUzbekistan from a dict
commission_uzbekistan_from_dict = CommissionUzbekistan.from_dict(commission_uzbekistan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



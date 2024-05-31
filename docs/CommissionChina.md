# CommissionChina


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**List[CommissionChinaReportInner]**](CommissionChinaReportInner.md) | Список комиссий | [optional] 

## Example

```python
from wildberries_async_api_client.models.commission_china import CommissionChina

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionChina from a JSON string
commission_china_instance = CommissionChina.from_json(json)
# print the JSON string representation of the object
print(CommissionChina.to_json())

# convert the object into a dict
commission_china_dict = commission_china_instance.to_dict()
# create an instance of CommissionChina from a dict
commission_china_from_dict = CommissionChina.from_dict(commission_china_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



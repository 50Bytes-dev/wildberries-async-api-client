# ModelsExciseReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ModelsExciseReportResponseDataInner]**](ModelsExciseReportResponseDataInner.md) |  | [optional] 

## Example

```python
from wildberries_async_api_client.models.models_excise_report_response import ModelsExciseReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsExciseReportResponse from a JSON string
models_excise_report_response_instance = ModelsExciseReportResponse.from_json(json)
# print the JSON string representation of the object
print(ModelsExciseReportResponse.to_json())

# convert the object into a dict
models_excise_report_response_dict = models_excise_report_response_instance.to_dict()
# create an instance of ModelsExciseReportResponse from a dict
models_excise_report_response_from_dict = ModelsExciseReportResponse.from_dict(models_excise_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApiV1FeedbacksReportGet200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Имя файла | [optional] 
**file** | **bytearray** | Файл | [optional] 
**content_type** | **str** | Тип контента | [optional] 

## Example

```python
from wildberries_async_api_client.models.api_v1_feedbacks_report_get200_response_data import ApiV1FeedbacksReportGet200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1FeedbacksReportGet200ResponseData from a JSON string
api_v1_feedbacks_report_get200_response_data_instance = ApiV1FeedbacksReportGet200ResponseData.from_json(json)
# print the JSON string representation of the object
print(ApiV1FeedbacksReportGet200ResponseData.to_json())

# convert the object into a dict
api_v1_feedbacks_report_get200_response_data_dict = api_v1_feedbacks_report_get200_response_data_instance.to_dict()
# create an instance of ApiV1FeedbacksReportGet200ResponseData from a dict
api_v1_feedbacks_report_get200_response_data_from_dict = ApiV1FeedbacksReportGet200ResponseData.from_dict(api_v1_feedbacks_report_get200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



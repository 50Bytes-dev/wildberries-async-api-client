# ContentV2BarcodesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов для генерации - &#x60;5 000&#x60; | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_barcodes_post_request import ContentV2BarcodesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2BarcodesPostRequest from a JSON string
content_v2_barcodes_post_request_instance = ContentV2BarcodesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV2BarcodesPostRequest.to_json())

# convert the object into a dict
content_v2_barcodes_post_request_dict = content_v2_barcodes_post_request_instance.to_dict()
# create an instance of ContentV2BarcodesPostRequest from a dict
content_v2_barcodes_post_request_from_dict = ContentV2BarcodesPostRequest.from_dict(content_v2_barcodes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



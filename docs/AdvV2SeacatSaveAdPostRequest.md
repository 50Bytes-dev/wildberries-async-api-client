# AdvV2SeacatSaveAdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_name** | **str** | Название кампании | [optional] 
**nms** | **List[int]** | Номенклатуры для кампании. Доступные номенклатуры можно получить с помощью метода [Номенклатуры для кампаний](./#tag/Slovari/paths/~1adv~1v2~1supplier~1nms/post). Максимум 50 товаров (&#x60;nm&#x60;)  | 

## Example

```python
from wildberries_async_api_client.models.adv_v2_seacat_save_ad_post_request import AdvV2SeacatSaveAdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvV2SeacatSaveAdPostRequest from a JSON string
adv_v2_seacat_save_ad_post_request_instance = AdvV2SeacatSaveAdPostRequest.from_json(json)
# print the JSON string representation of the object
print(AdvV2SeacatSaveAdPostRequest.to_json())

# convert the object into a dict
adv_v2_seacat_save_ad_post_request_dict = adv_v2_seacat_save_ad_post_request_instance.to_dict()
# create an instance of AdvV2SeacatSaveAdPostRequest from a dict
adv_v2_seacat_save_ad_post_request_from_dict = AdvV2SeacatSaveAdPostRequest.from_dict(adv_v2_seacat_save_ad_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ContentV2TagNomenclatureLinkPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nm_id** | **int** | Артикул WB | [optional] 
**tags_ids** | **List[int]** | Массив числовых идентификаторов тегов.&lt;br&gt;   Что бы снять теги с КТ, необходимо передать пустой массив.&lt;br&gt; Чтобы добавить теги к уже имеющимся в КТ, необходимо в запросе передать новые теги и теги, которые уже есть в КТ.  | [optional] 

## Example

```python
from wildberries_async_api_client.models.content_v2_tag_nomenclature_link_post_request import ContentV2TagNomenclatureLinkPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContentV2TagNomenclatureLinkPostRequest from a JSON string
content_v2_tag_nomenclature_link_post_request_instance = ContentV2TagNomenclatureLinkPostRequest.from_json(json)
# print the JSON string representation of the object
print(ContentV2TagNomenclatureLinkPostRequest.to_json())

# convert the object into a dict
content_v2_tag_nomenclature_link_post_request_dict = content_v2_tag_nomenclature_link_post_request_instance.to_dict()
# create an instance of ContentV2TagNomenclatureLinkPostRequest from a dict
content_v2_tag_nomenclature_link_post_request_from_dict = ContentV2TagNomenclatureLinkPostRequest.from_dict(content_v2_tag_nomenclature_link_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


